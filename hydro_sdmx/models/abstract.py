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

class NameableArtefact(IdentifiableArtefact):
    name = models.CharField(
        max_length=maxlengths.NAME, blank=True,
    )
    description = models.TextField(blank=True)

    class Meta(IdentifiableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['name']),
            models.Index(fields=['id_code', 'name']),
        ]

    def __str__(self):
        return '%s - %s' % (self.id_code, self.name)

class Item(NameableArtefact):
    wrapper = models.ForeignKey('MaintainableArtefact', on_delete=models.CASCADE)

    class Meta(NameableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['wrapper']),
            models.Index(fields=['wrapper', 'id_code']),
            models.Index(fields=['wrapper', 'name']),
        ]
        unique_together = ('wrapper', 'id_code')

class RepresentedItem(Item):
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
    is_multiLingual = models.NullBooleanField(null=True, blank=True)

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

class VersionableArtefact(NameableArtefact):
    version = models.CharField(
        max_length=maxlengths.VERSION, 
        validators=[re_validators['VersionType']], 
        default='1.0'
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta(NameableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['id_code', 'version']),
            models.Index(fields=['id_code', 'name', 'version']),
        ]

class MaintainableArtefact(VersionableArtefact):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[re_validators['IDType']])
    agency = models.ForeignKey('Organisation', on_delete=models.CASCADE) 
    is_final = models.BooleanField(default=False)
    name = models.CharField(max_length=maxlengths.NAME)
    registrations = models.ManyToManyField(Registration)

    class Meta(VersionableArtefact.Meta):
        abstract = True
        unique_together = ('id_code', 'agency', 'version')
        indexes = [
            models.Index(fields=['id_code']),
            models.Index(fields=['name']),
            models.Index(fields=['agency']),
            models.Index(fields=['id_code', 'version']),
            models.Index(fields=['id_code','agency', 'version']),
        ]

    def __str__(self):
        return '%s:%s:%s:%s' % (self.id_code, self.agency, self.version, self.name)

    def clean(self):
        # Make sure that final structures cannot be modified
        created = not bool(self.pk)
        if not created and self.is_final:
            raise clean_validators['MaintainableArtefact']['update']
        created_by = get_current_user()
        if not hasattr(created_by, 'contact') and not created_by.is_superuser:
            raise clean_validators['MaintainableArtefact']['contact']

    def save(self, *args, **kwargs):
        if not kwargs.get('registration'):
            created = not bool(self.pk)
            action = 'Append' if created else 'Replace'
            created_by = get_current_user()
            registration = Registration(created_by=created_by, action=action, interactive=True)
            registration.save()
            kwargs['registration'] = registration 
        self.full_clean()
        registration = kwargs.pop('registration')
        super().save(*args, **kwargs)
        self.registrations.add(registration)

    def delete(self):
        #improve this by creating a delete flag on maintaintable artefacts and only allow administrators of the maintainable agency, as well as super users to perform this action
        #the code below makes a delete registration but removes completely the artefact so no historicity is kept
        action = 'Delete'
        created_by = get_current_user()
        Registration(created_by=created_by, action=action, interactive=True).save()
        super().delete()

# class Item(NameableArtefact):
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#
# class ItemWithParent(Item, MP_Node):
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta(Item.Meta):
#         abstract = True
#
#     def save(self, **kwargs):
#         if not self.depth:
#             if self.parent_id:
#                 self.depth = self.parent.depth + 1
#                 self.parent.add_child(instance=self)
#             else:
#                 self.add_root(instance=self)
#             return  #add_root and add_child save as well
#         super().save(**kwargs)
# from django.core.exceptions import ValidationError
# from django.db import models
#
# from treebeard.mp_tree import MP_Node
#
# from ..settings import api_maxlen_settings 
# from ..validators import re_validators, errors 
#
# class AnnotableArtefact(models.Model):
#     annotations = models.ManyToManyField('Annotation', related_name='+')
#
#     class Meta:
#         abstract = True
#
# class IdentifiableArtefact(AnnotableArtefact):
#     uri = models.URLField('URI', null=True, blank=True)
#     id_code = models.CharField(
#         'ID', max_length=api_maxlen_settings.ID_CODE, 
#         validators=[re_validators['IDType']], 
#         blank=True,
#     )
#
#     class Meta:
#         abstract = True
#         ordering = ['id_code']
#         indexes = [
#             models.Index(fields=['id_code']),
#         ]
#
#     def __str__(self):
#         return self.id_code 
#
# class StructureItem(IdentifiableArtefact):
#
#     class Meta(IdentifiableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['wrapper']),
#         ]
#         unique_together = ('wrapper', 'id_code', 'concept')
#
# class NameableArtefact(IdentifiableArtefact):
#     name = models.CharField(
#         max_length=api_maxlen_settings.NAME, blank=True,
#     )
#     description = models.TextField(blank=True)
#
#     class Meta(IdentifiableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['name']),
#             models.Index(fields=['id_code', 'name']),
#         ]
#
#     def __str__(self):
#         return '%s - %s' % (self.id_code, self.name)
#
# class Item(NameableArtefact):
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['wrapper']),
#             models.Index(fields=['wrapper', 'id_code']),
#             models.Index(fields=['wrapper', 'name']),
#         ]
#         unique_together = ('wrapper', 'id_code')
#
#
# class ItemWithParent(Item, MP_Node):
#
#     class Meta(Item.Meta):
#         abstract = True
#
#     def clean(self):
#         if self.parent:
#             if self.wrapper != self.parent.wrapper:
#                 raise ValidationError({
#                     'parent': errors['parent'],
#                 })
#
#     def save(self, **kwargs):
#         if not self.depth:
#             if self.parent_id:
#                 self.depth = self.parent.depth + 1
#                 self.parent.add_child(instance=self)
#             else:
#                 self.add_root(instance=self)
#             return  #add_root and add_child save as well
#         super().save(**kwargs)
#
# class VersionableArtefact(NameableArtefact):
#     version = models.CharField(
#         max_length=api_maxlen_settings.VERSION, 
#         validators=[re_validators['VersionType']], 
#         default='1.0'
#     )
#     valid_from = models.DateTimeField(null=True, blank=True)
#     valid_to = models.DateTimeField(null=True, blank=True)
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['id_code', 'version']),
#             models.Index(fields=['id_code', 'name', 'version']),
#         ]
#
#     def __str__(self):
#         return 'id:%s, id_code:%s, version:%s, name:%s' % (self.id_code, self.version, self.name)
