from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from django.urls import reverse
from hvad.models import TranslatableModel, TranslatedFields
from common.constants import max_length

from structure.models import Item, ItemScheme 
from common.validators import re_validators

#Organisation Structure

class OrganisationScheme(ItemScheme):
    translations = TranslatedFields()

    def clean(self):
        if self.id_code in ['AGENCIES', 'DATA_CONSUMERS', 'DATA_PROVIDERS'] \
           and self.version != '1.0':
                raise ValidationError({
                    'version': ValidationError(
                        _('Version must be 1.0'), code='version'
                    ),
                })
        if self.id_code in ['AGENCIES', 'DATA_CONSUMERS', 'DATA_PROVIDERS'] \
           and self.isFinal:
                raise ValidationError({
                    'isFinal': ValidationError(
                        _('Cannot be Final'), code='final'
                    ),
                })

    def get_absolute_url(self):
        return reverse('organisationScheme-detail', kwargs={'pk': self.pk})

class Organisation(Item):
    organisationScheme = models.ForeignKey(
        OrganisationScheme, on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )
    translations = TranslatedFields()

    class Meta:
        unique_together = ('organisationScheme', 'id_code')

    def clean(self):
        if self.parent:
            if self.organisationScheme != self.parent.organisationScheme:
                raise ValidationError({
                    'parent': ValidationError(
                        _('''Parent and child Organisations must belong in the \
                          same OrganisationScheme'''), code='local'
                    ),
                })

class Contact(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True),
        department = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True),
        role = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True)
    )
    telephone = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    fax = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    x400 = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    uRI = ArrayField(models.URLField(null=True, blank=True),  null=True, blank=True)
    email = ArrayField(models.EmailField(null=True, blank=True),  null=True, blank=True)
    #deviates from SDMX Information Model and make this required and unique
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        unique=True
    )
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

