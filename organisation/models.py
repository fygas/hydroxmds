from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from django.urls import reverse

from structure.models import ItemScheme, Organisation

class OrganisationScheme(ItemScheme):
    organisations = models.ManyToManyField(
        Organisation, related_name = 'schemes' 
    )
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
