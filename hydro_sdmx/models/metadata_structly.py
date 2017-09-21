from django.contrib.contenttypes.models import ContentType
from django.db import models

from .abstract import IdentifiableArtefact, StructureItem
from .abstract_postorg import MaintainableArtefact
from .codelist import Representation
from .common import Annotation 
from .conceptscheme import Concept

from ..constants import METADATA_TARGET_TYPES 
from ..settings import api_maxlen_settings
from ..validators import re_validators 


class MetadataStructure(MaintainableArtefact):
    target_annotations = models.ManyToManyField(Annotation, related_name='+')
    report_annotations = models.ManyToManyField(Annotation, related_name='+')
    reports = models.ManyToManyField('Report')

class Metadataflow(MaintainableArtefact):
    structure = models.ForeignKey(MetadataStructure)

class MetadataTarget (IdentifiableArtefact):
    structure = models.ForeignKey(MetadataStructure, related_name='targets')
    components = models.ManyToManyField('MetadataTargetComponent')

    class Meta(IdentifiableArtefact.Meta):
        unique_together = ('id_code', 'structure')

class MetadataTargetComponent(IdentifiableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
    )
    component_type = models.CharField(max_length=api_maxlen_settings.METADATA_TARGET_COMPONENTS, choices=METADATA_TARGET_TYPES) 
    identifiable_object = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta(IdentifiableArtefact.Meta):
        unique_together = ('id_code', 'component_type', 'identifiable_object')

class Report(MaintainableArtefact):
    targets = models.ManyToManyField('MetadataTarget')
    metadata_attributes = models.ManyToManyField(Concept, through='MetadataAttribute', related_name='reports')

class MetadataAttribute(StructureItem):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='metadata_attributes')
    wrapper = models.ForeignKey(Report, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='metadata_attributes')
    min_occurs = models.IntegerField(default=1)
    max_occurs = models.IntegerField(default=1)
    is_presentational = models.BooleanField(default=False)
