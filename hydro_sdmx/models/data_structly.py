from django.db import models

from .abstract import AnnotableArtefact, IdentifiableArtefact, StructureItem
from .abstract_postorg import MaintainableArtefact
from .codelist import Representation 
from .common import Annotation
from .conceptscheme import Concept, ConceptScheme

from ..constants import DIMENSION_TYPES 
from ..settings import api_maxlen_settings

class DataStructure(MaintainableArtefact):
    dimension_annotations = models.ManyToManyField(Annotation, related_name='+')
    measure_annotations = models.ManyToManyField(Annotation, related_name='+')
    attribute_annotations = models.ManyToManyField(Annotation, related_name='+')
    dimensions = models.ManyToManyField(Concept, through='Dimension')
    obs_value = models.ForeignKey('ObsValue', on_delete=models.CASCADE, related_name='dsds')
    attributes = models.ManyToManyField(Concept, through='Attribute')
    groups = models.ManyToManyField('Group', related_name='dsds')

class Dataflow(MaintainableArtefact):
    structure = models.ForeignKey(DataStructure)

class Group(IdentifiableArtefact):
    
    # It can either be a group of dimensions backward relationship with Dimension.groups
    # field or an attachment_constraint group
    attachment_constraint = models.ForeignKey('AttachmentConstraint', null=True, blank=True, on_delete=models.CASCADE, related_name='groups')

    class Meta(IdentifiableArtefact.Meta):
        unique_together = ('id_code', 'attachment_constraint')

class Dimension(StructureItem):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    wrapper = models.ForeignKey(DataStructure, verbose_name='DSD', on_delete=models.CASCADE)
    dimension_type = models.CharField(max_length=api_maxlen_settings.DIMENSION_TYPE, choices=DIMENSION_TYPES)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='dimensions')
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, null=True, blank=True, related_name='measure_dimensions')
    roles = models.ManyToManyField(Concept, related_name='role_for_dimensions')
    groups = models.ManyToManyField(Group, related_name='dimensions')

    def __str__(self):
        return '%s - %s' % (self.id_code, self.wrapper)

class ObsValue(AnnotableArtefact):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_obs_values')
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='obs_values')

class Attribute(StructureItem):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_attributes')
    wrapper = models.ForeignKey(DataStructure, verbose_name='DSD', on_delete=models.CASCADE)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='attributes')
    roles = models.ManyToManyField(Concept, related_name='role_for_attributes')
    required = models.BooleanField(default=True)
    attached2dims = models.ManyToManyField(Dimension, related_name='attached_attributes')
    attached2measure = models.BooleanField(default=False)
    attached2dim_in_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='attached_attributes2each_group_dim')
    attached2groups = models.ManyToManyField(Group, related_name='attached_attributes')
