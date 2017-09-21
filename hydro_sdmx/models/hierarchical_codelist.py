from django.db import models

from .abstract import IdentifiableArtefact, NameableArtefact
from .abstract_postorg import MaintainableArtefact
from .codelist import Code, TextFormatInfo

from ..settings import api_maxlen_settings 
from ..validators import re_validators 

class HierarchicalNameableArtefact(NameableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
    )
    name = models.CharField(max_length=api_maxlen_settings.NAME)

    class Meta(NameableArtefact.Meta):
        abstract = True

class HierarchicalCodelist(MaintainableArtefact):
    hierarchies = models.ManyToManyField('Hierarchy')

class Hierarchy(HierarchicalNameableArtefact):
    level = models.ForeignKey('Level', null=True, blank=True, on_delete=models.CASCADE)
    hierarchical_codes = models.ManyToManyField('HierarchicalCode')
    leveled = models.BooleanField(default=False)

class HierarchicalCode(IdentifiableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE, 
        validators=[re_validators['IDType']], 
    )
    code = models.ForeignKey(Code)
    children = models.ManyToManyField('self')
    depth = models.IntegerField()
    level = models.IntegerField(null=True, blank=True)
    version = models.CharField(
        max_length=api_maxlen_settings.VERSION, 
        validators=[re_validators['VersionType']]
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

class Level(HierarchicalNameableArtefact):
    coding_format = models.ForeignKey(TextFormatInfo, null=True, blank=True, on_delete=models.CASCADE)
    level = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    depth = models.IntegerField() #0 is top level
