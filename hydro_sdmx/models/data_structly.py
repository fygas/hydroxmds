from django.db import models

from .abstract import MaintainableArtefact, BaseRepresentation, RepresentedItem
from .conceptscheme import Concept, ConceptScheme

from ..constants import DIMENSION_TYPES 
from ..settings import api_maxlen_settings as maxlengths

class GroupID(models.Model):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               unique=True)
class DataStructure(MaintainableArtefact, BaseRepresentation):
    # Will not include annotation fields for component_sets.  There are
    # many other places to add annotations if someone feels like a need 
    wrapper = None
    dimensions = models.ManyToManyField(Concept, through='Dimension', related_name='dimensions')
    groups = models.ManyToManyField(GroupID, through='Group', blank=True)
    attributes = models.ManyToManyField(Concept, through='Attribute', related_name='+', blank=True)
    obs_concept = models.ForeignKey('Concept', on_delete=models.CASCADE, related_name='+')

class Dataflow(MaintainableArtefact):
    structure = models.ForeignKey(DataStructure)

class Group(models.Model):
    group_id = models.ForeignKey(GroupID, on_delete=models.CASCADE)
    data_structure = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    dimensions = models.ManyToManyField('Dimension', blank=True)
    attachment_constraint = models.ForeignKey('AttachmentConstraint', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    #This field will be used as a flag of extra groups that use additional attachment constraints to report documentation but are not in the data structure definition
    extra = models.BooleanField(default=False)

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
    dimension_type = models.CharField(max_length=maxlengths.DIMENSION_TYPE, choices=DIMENSION_TYPES)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_concept_role = models.BooleanField(default=True)
    measure_representation = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    roles = models.ManyToManyField('Concept', related_name='+', blank=True)

class Attribute(Component):
    is_concept_role = models.BooleanField(default=True)
    roles = models.ManyToManyField('Concept', related_name='role_for_attributes', blank=True)
    required = models.BooleanField(default=True)
    attached2dataset = models.BooleanField(default=False)
    attached2group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='full_attachment')
    attached2dimensions = models.ManyToManyField(Dimension, blank=True)
    associated_groups = models.ManyToManyField(Group, blank=True, related_name='attributes')
    attached2measure = models.BooleanField(default=False)
