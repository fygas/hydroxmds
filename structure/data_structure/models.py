from django.db import models

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
    dimensions = models.ManyToManyField(Concept, through='Dimension', through_fields=('concept', 'dsd'))
    time_dimension = models.ForeignKey('TimeDimension', null=True, blank=True, on_delete=models.CASCADE)
    measure_dimension = models.ForeignKey('MeasureDimension', null=True, blank=True, on_delete=models.CASCADE)
    obs_value = models.ForeignKey('ObsValue', on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Concept, through='Attribute')
    groups = models.ManyToManyField('DimensionGroup')

class DimensionGroup(IdentifiableArtefact):
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='dimensions')
    class Meta:
        unique_together = ('id_code', 'dsd')

class Dimension(IdentifiableArtefact):
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='dimensions')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_dimensions')
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='dimensions')
    roles = models.ManyToManyField(Concept, related_name='role_for_dimensions')
    groups = models.ManyToManyField(DimensionGroup, related_name='dimensions')
    
    class Meta:
        unique_together = ('id_code', 'dsd', 'concept')

class TimeDimension(AnnotableArtefact):
    dsd = models.OneToOneField(DataStructure, on_delete=models.CASCADE, related_name='time_dimension')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_time_dimensions')
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='dimensions')
    roles = models.ManyToManyField(Concept, related_name='role_for_measure_dimensions')
    groups = models.ManyToManyField(DimensionGroup, related_name='measure_dimension')

class MeasureDimension(IdentifiableArtefact):
    dsd = models.OneToOneField(DataStructure, on_delete=models.CASCADE, related_name='measure_dimension')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_measure_dimensions')
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, related_name='measure_dimensions')
    roles = models.ManyToManyField(Concept, related_name='role_for_measure_dimensions')
    groups = models.ManyToManyField(DimensionGroup, related_name='measure_dimension')

class ObsValue(AnnotableArtefact):
    dsd = models.OneToOneField(DataStructure, on_delete=models.CASCADE, related_name='obs_value')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_obs_values')
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='obs_values')

class ReportingYearStartDate(AnnotableArtefact):
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='reporting_time_period')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_attributes')
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='attributes')
    required = models.BooleanField(default=False)

class Attribute(IdentifiableArtefact):
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='attributes')
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_attributes')
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='attributes')
    roles = models.ManyToManyField(Concept, related_name='role_for_attributes')
    required = models.BooleanField(default=True)
    attached2dims = models.ManyToManyField(Dimension, related_name='attached_attributes')
    attached2measure = models.BooleanField(default=False)
    attached2dim_in_group = models.ForeignKey(DimensionGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='attached_attributes2each_group_dim')
    attached2groups = models.ManyToManyField(DimensionGroup, related_name='attached_attributes')
    
    class Meta:
        unique_together = ('id_code', 'dsd', 'concept')
