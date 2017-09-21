from django.db import models

from .abstract import IdentifiableArtefact, NameableArtefact, ItemWithParent
from .abstract_postorg import MaintainableArtefact

from ..constants import DATA_TYPES 
from ..settings import api_maxlen_settings 
from ..validators import re_validators 


#Concrete models
class Codelist(MaintainableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE, \
        validators=[re_validators['NCNameIDType']], \
    )

class Code(ItemWithParent):
    wrapper = models.ForeignKey(Codelist, verbose_name='Codelist', on_delete=models.CASCADE, related_name='codes')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )

class TextFormatInfo(NameableArtefact):
    annotations = None
    uri = None
    description = None
    text_type = models.CharField(
        max_length=api_maxlen_settings.DATA_TYPE, 
        blank=True, 
        choices=DATA_TYPES
    )
    is_sequence = models.NullBooleanField(null=True)
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

    def __str__(self):
        '%s-%s-%s' % (self.id_code, self.name, self.text_type)


class Representation(IdentifiableArtefact):
    text_format = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    enumeration = models.ForeignKey(Codelist, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    enumeration_format = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')

    def __str__(self):
        if self.text_format:
            return 'Text Format: %s-%s' % (self.text_format.id_code, self.text_format.name)
        else:
            return 'Enumeration: %s-%s' % (self.enumeration.id_code, self.enumeration.name)
