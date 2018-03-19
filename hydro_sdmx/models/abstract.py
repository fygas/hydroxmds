from django.core.exceptions import ValidationError
from django.db import models

from treebeard.mp_tree import MP_Node

from .registration import Registration 
from ..settings import api_maxlen_settings as maxlengths 
from ..validators import re_validators, errors, clean_validators
from ..constants import DATA_TYPES 
from ..settings import api_maxlen_settings 
from ..utils.permissions import get_current_user

class IdentifiableArtefact(models.Model):
    uri = models.URLField('URI', null=True, blank=True)
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[re_validators['IDType']],
                               blank=True)

    class Meta:
        abstract = True
        ordering = ['id_code']
        indexes = [
            models.Index(fields=['id_code']),
        ]

    def __str__(self):
        return self.id_code 

class Item(IdentifiableArtefact):
    wrapper = models.ForeignKey('MaintainableArtefact', on_delete=models.CASCADE)

    class Meta(IdentifiableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['wrapper']),
            models.Index(fields=['wrapper', 'id_code']),
        ]
        unique_together = ('wrapper', 'id_code')

class BaseRepresentation(models.Model):

    enumeration = models.ForeignKey('Codelist', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    text_type = models.CharField(
        max_length=api_maxlen_settings.DATA_TYPE, 
        blank=True, 
        choices=DATA_TYPES
    )
    is_sequence = models.NullBooleanField(null=True, blank=True)
    interval = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    start_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    end_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    time_interval = models.DurationField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    min_length = models.PositiveIntegerField(null=True, blank=True)
    max_length = models.PositiveIntegerField(null=True, blank=True)
    min_value= models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    max_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    decimals = models.PositiveIntegerField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    is_multi_lingual = models.NullBooleanField(null=True, blank=True)

    class Meta(Item.Meta):
        abstract = True

class RepresentedItem(Item, BaseRepresentation):
    class Meta(Item.Meta):
        abstract = True

class ItemWithParent(Item, MP_Node):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True)

    class Meta(Item.Meta):
        abstract = True

    def clean(self):
        if self.parent:
            if self.wrapper != self.parent.wrapper:
                raise ValidationError({
                    'parent': errors['parent'],
                })

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)

class RepresentedItemWithParent(RepresentedItem, MP_Node):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True)

    class Meta(Item.Meta):
        abstract = True

    def clean(self):
        if self.parent:
            if self.wrapper != self.parent.wrapper:
                raise ValidationError({
                    'parent': errors['parent'],
                })

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)

class VersionableArtefact(IdentifiableArtefact):
    version = models.CharField(
        max_length=maxlengths.VERSION, 
        validators=[re_validators['VersionType']], 
        default='1.0'
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta(IdentifiableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['id_code', 'version']),
        ]

class Action(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not kwargs.get('registration'):
            created = not bool(self.pk)
            action = 'A' if created else 'R'
            registrant = get_current_user()
            registration = Registration(registrant=registrant, action=action, interactive=True)
            registration.save()
            kwargs['registration'] = registration 
            self.pk = None
        self.full_clean()
        self.registration = kwargs.pop('registration')
        super().save(*args, **kwargs)

    def delete(self):
        action = 'D'
        registrant = get_current_user()
        self.registration = Registration(registrant=registrant, action=action, interactive=True).save()
        self.pk = None
        super().save()

class MaintainableArtefact(Action, VersionableArtefact):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[re_validators['IDType']])
    agency = models.ForeignKey('Organisation', on_delete=models.CASCADE) 
    is_final = models.BooleanField(default=False)
    registration = models.ForeignKey(Registration, editable=False)

    class Meta(VersionableArtefact.Meta):
        abstract = True
        unique_together = ('id_code', 'agency', 'version', 'registration')
        indexes = [
            models.Index(fields=['id_code']),
            models.Index(fields=['agency']),
            models.Index(fields=['id_code', 'version']),
            models.Index(fields=['id_code','agency', 'version']),
        ]

    def __str__(self):
        return '%s:%s:%s' % (self.id_code, self.agency, self.version)

    def clean(self):
        # Make sure that final structures cannot be modified
        created = not bool(self.pk)
        if not created and self.is_final:
            raise clean_validators['MaintainableArtefact']['update']
        created_by = get_current_user()
        if not hasattr(created_by, 'contact') and not created_by.is_superuser:
            raise clean_validators['MaintainableArtefact']['contact']
