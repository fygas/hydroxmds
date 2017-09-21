from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import DateTimeRangeField 

from base.constants import dimension_types
from base.models import (
    Annotation, AnnotableArtefact, MaintainableArtefact, Concept,
    ConceptScheme, IdentifiableArtefact, Representation, Code
)

class DataStructure(MaintainableArtefact):
    dimension_annotations = models.ManyToManyField(Annotation, related_name='+')
    measure_annotations = models.ManyToManyField(Annotation, related_name='+')
    attribute_annotations = models.ManyToManyField(Annotation, related_name='+')
    dimensions = models.ManyToManyField(Concept, through='Dimension', related_name='dimensions')
    obs_value = models.ForeignKey('ObsValue', on_delete=models.CASCADE, related_name='dsds')
    attributes = models.ManyToManyField(Concept, through='Attribute', related_name='attributes')
    groups = models.ManyToManyField('Group', related_name='dsds')

class Dataflow(MaintainableArtefact):
    structure = models.ForeignKey(DataStructure)

class Group(IdentifiableArtefact):
    
    # It can either be a group of dimensions backward relationship with Dimension.groups
    # field or an attachment_constraint group
    attachment_constraint = models.ForeignKey('DataConstraint', null=True, blank=True, on_delete=models.CASCADE, related_name='groups')
    class Meta:
        unique_together = ('id_code', 'attachment_constraint')

class Dimension(IdentifiableArtefact):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_dimensions')
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    dimension_type = models.CharField(max_length=settings.MAX_LENGTH, choices=dimension_types)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='dimensions')
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, null=True, blank=True, related_name='measure_dimensions')
    roles = models.ManyToManyField(Concept, related_name='role_for_dimensions')
    groups = models.ManyToManyField(Group, related_name='dimensions')
    
    class Meta:
        unique_together = ('id_code', 'dsd', 'concept')

class ObsValue(AnnotableArtefact):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_obs_values')
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='obs_values')

class Attribute(IdentifiableArtefact):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='concept_for_attributes')
    dsd = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    is_concept_role = models.BooleanField(default=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='attributes')
    roles = models.ManyToManyField(Concept, related_name='role_for_attributes')
    required = models.BooleanField(default=True)
    attached2dims = models.ManyToManyField(Dimension, related_name='attached_attributes')
    attached2measure = models.BooleanField(default=False)
    attached2dim_in_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='attached_attributes2each_group_dim')
    attached2groups = models.ManyToManyField(Group, related_name='attached_attributes')
    
    class Meta:
        unique_together = ('id_code', 'dsd', 'concept')

class DataConstraint(MaintainableArtefact):
    attached2dsds = models.ManyToManyField(DataStructure)
    attached2dataflows = models.ManyToManyField(Dataflow)

class DataKeySet(models.Model):
    constraint = models.ForeignKey(DataConstraint, on_delete=models.CASCADE, related_name='data_key_sets')
    data_key_set_code = models.IntegerField()

    class Meta:
        unique_together = ('constraint', 'data_key_set_code')

class DataKey(models.Model):
    data_key_set = models.ForeignKey(DataKeySet, on_delete=models.CASCADE, related_name='data_keys')
    data_key_code = models.IntegerField()
    is_included = models.BooleanField(default=True)

    class Meta:
        unique_together = ('data_key_set', 'data_key_code')

class KeyValue(models.Model):
    data_key = models.ForeignKey(DataKey, on_delete=models.CASCADE, related_name='key_values')
    # In the following the dimension is linked to a specific dimension of
    # a DSD.  We are not though interested on that specific DSD.  We are
    # interested only at the id_code of the dimension, since a constraint
    # can be attached to many dataflows or DSDs that have a dimension with
    # identical identifier.
    dimension = models.ForeignKey(Dimension)
    value = models.ForeignKey(Code, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('data_key', 'dimension', 'value')
    
class CubeRegion(models.Model):
    constraint = models.ForeignKey(DataConstraint, on_delete=models.CASCADE, related_name='cube_regions')
    cube_region_code = models.IntegerField()
    include = models.BooleanField(default=True)

    class Meta:
        unique_together = ('constraint', 'cube_region_code')

class KeyValueSet(models.Model):
    cube_region = models.ForeignKey(CubeRegion, on_delete=models.CASCADE, related_name='data_keys')
    # In the following the dimension is linked to a specific dimension of
    # a DSD.  We are not though interested on that specific DSD.  We are
    # interested only at the id_code of the dimension, since a constraint
    # can be attached to many dataflows or DSDs that have a dimension with
    # identical identifier.
    dimension = models.ForeignKey(Dimension)
    values = models.ManyToManyField(Code)
    time_range = DateTimeRangeField(null=True, blank=True)

    class Meta:
        unique_together = ('cube_region', 'dimension')
