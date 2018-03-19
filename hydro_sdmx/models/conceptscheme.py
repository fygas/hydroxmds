from django.db import models

from .abstract import RepresentedItemWithParent, MaintainableArtefact

from ..settings import api_maxlen_settings
from ..validators import re_validators 

class ConceptScheme(MaintainableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['NCNameIDType']],
    )

class Concept(RepresentedItemWithParent):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
    )
    wrapper = models.ForeignKey(ConceptScheme, verbose_name='Concept Scheme', on_delete=models.CASCADE)
    iso_concept_reference = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
