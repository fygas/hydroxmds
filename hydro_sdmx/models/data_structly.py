from django.db import models

from .abstract import MaintainableArtefact, RepresentedItem
from .conceptscheme import Concept, ConceptScheme

from ..constants import DIMENSION_TYPES 
from ..settings import api_maxlen_settings

class DataStructure(MaintainableArtefact):
    # Will not include annotation fields for component_sets.  There are
    # many other places to add annotations if one feels like it!!!
    dimensions = models.ManyToManyField(Concept, through='Dimension', related_name='dimensions')
    measures = models.ManyToManyField(Concept, through='Measure', related_name='+')
    attributes = models.ManyToManyField(Concept, through='Attribute', related_name='+')

class Dataflow(MaintainableArtefact):
    structure = models.ForeignKey(DataStructure)

    # It can either be a group of dimensions backward relationship with Dimension.groups
    # field or an attachment_constraint group
class Group(models.Model):
    id_code = models.CharField('ID', max_length=api_maxlen_settings.ID_CODE,
                               unique=True)
    # structure = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='groups')
    
    # attachment_constraint = models.ForeignKey('AttachmentConstraint', null=True, blank=True, on_delete=models.CASCADE, related_name='+')

class Component(RepresentedItem):
    description = None
    name = None
    concept = models.ForeignKey('Concept', on_delete=models.CASCADE, related_name='+')
    wrapper = models.ForeignKey(DataStructure, verbose_name='DSD', on_delete=models.CASCADE, related_name='+')
    class Meta:
        abstract = True
        unique_together = ['id_code', 'concept', 'wrapper'] 

    def __str__(self):
        return '%s:%s:%s' % (self.id_code, self.concept, self.wrapper)

class Dimension(Component):
    dimension_type = models.CharField(max_length=api_maxlen_settings.DIMENSION_TYPE, choices=DIMENSION_TYPES)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    roles = models.ManyToManyField('Concept', related_name='+')
    groups = models.ManyToManyField(Group, related_name='dimensions')

class Measure(Component):
    pass

class Attribute(Component):
    is_concept_role = models.BooleanField(default=True)
    roles = models.ManyToManyField('Concept', related_name='role_for_attributes')
    required = models.BooleanField(default=True)
    attached2dims = models.ManyToManyField(Dimension, related_name='attached_attributes')
    attached2measure = models.BooleanField(default=False)
    attached2dim_in_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='attached_attributes2each_group_dim')
    attached2groups = models.ManyToManyField(Group, related_name='attached_attributes')
