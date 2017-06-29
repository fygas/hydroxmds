from django.db import models
from ..constants import object_types
from django.conf import settings

from common.models import Annotation, AnnotableArtefact
from ..models import (
    MaintainableArtefact, Concept, ConceptScheme,
    IdentifiableArtefact, Representation,
)

#DataStructure Structure

class DataStructure(MaintainableArtefact):
    dimension_annotations = models.ManyToManyField(Annotation, related_name='+')
    measure_annotations = models.ManyToManyField(Annotation, related_name='+')
    attribute_annotations = models.ManyToManyField(Annotation, related_name='+')
    components = models.ManyToManyField('DataStructureComponent')
    groups = models.ManyToManyField('DataStructureComponentGroup')

class DataStructureComponentBase(IdentifiableArtefact):
    annotations = None
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='+')
    object_type = models.CharField(max_length=settings.MAX_LENGTH, choices = object_types, null=True, blank=True)
    class Meta:
        unique_together = ('id_code', 'concept')

class DataStructureComponentGroup(IdentifiableArtefact):
    group = models.ManyToManyField(DataStructureComponentBase)

class DataStructureComponent(AnnotableArtefact):
    id_code = None
    base_component = models.ForeignKey(DataStructureComponentBase, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    roles = models.ManyToManyField(Concept, related_name='+')
    dims_attached = models.ManyToManyField('self', related_name='+')
    primary_measure_attached = models.BooleanField(default=False)
    group = models.ForeignKey(DataStructureComponentGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='comp_group')
    groups = models.ManyToManyField(DataStructureComponentGroup, related_name='comp_groups')
