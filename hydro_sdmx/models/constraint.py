from django.db import models

from .abstract import MaintainableArtefact 
from .codelist import Code
from .data_structly import Dataflow, DataStructure 
from .provision import DataProvisionAgreement
from .organisation import Organisation
from .registration import Source 

from ..managers.constraint import (
    ConstraintDataKeyManager, KeyValueManager, ContentConstraintManager, 
    AttachmentConstraintManager,  DataKeySetManager, CodeValueDetailManager,
)
from ..settings import api_maxlen_settings as maxlengths 

class Constraint(MaintainableArtefact):
    datasets = models.ManyToManyField(Dataflow, related_name='dataset_attachment_constraints')
    datasources = models.ManyToManyField(Source, blank=True, related_name='attachment_constraints')

    class Meta(MaintainableArtefact.Meta):
        abstract = True

    def attached2ids(self, attachset):
        return (attach.id_code for attach in self.get(attachset))

    def provision_set(self):
        return self.attached2ids('provisions')

class AttachmentConstraint(Constraint):
    #intuition of AttachmentConstraint as far as I understand...
    #Attachment constraints allows someone to present the same data differently, ie more compact or less compact, by generating partial data keysets for which their attribute values remain unchanged.
    #AttachmentConstraints can be attached on the dataset level, the dataflow level, the datastructure level, the provisional agreement level and the datasource level.
    #Thus attachment constraints attached to related structures can be more or less restrictive based on the type of attachment level, with the less restrictive to be for the dataset level and the most restrictive to the datasource level
    data_structures = models.ManyToManyField(DataStructure, related_name='attachemt_constraints', blank=True)
    dataflows = models.ManyToManyField(Dataflow, related_name='dataflow_attachment_constraints', blank=True)
    provisions = models.ManyToManyField(DataProvisionAgreement, blank=True, related_name='attachment_constraints')

    objects = AttachmentConstraintManager()

    def data_structure_set(self):
        return self.attached2ids('data_structures')
    def dataflow_set(self):
        return self.attached2ids('dataflows')
    def datasource_set(self):
        return self.attached2ids('datasources')
    def dataset_set(self):
        return self.attached2ids('datasets')

class ContentConstraint(Constraint):
    provisions = models.ManyToManyField(DataProvisionAgreement, blank=True, related_name='content_constraints')
    dataproviders = models.ManyToManyField(Organisation, related_name='content_constraints', blank=True)
    data_structures = models.ManyToManyField(DataStructure, related_name='content_constraints', blank=True)
    dataflows = models.ManyToManyField(Dataflow, related_name='dataflow_content_constraints', blank=True)
    datasets = None 
    dataset = models.ForeignKey(Dataflow, null=True, blank=True, on_delete=models.CASCADE, related_name='dataset_content_constraints') 
    datasources = None
    datasource = models.ForeignKey(Source, null=True, blank=True, on_delete=models.CASCADE, related_name='content_constraints') 
    periodicity = models.CharField(max_length=maxlengths.PERIODICITY, blank=True)
    offset = models.CharField(max_length=maxlengths.OFFSET, blank=True)
    tolerance = models.CharField(max_length=maxlengths.TOLERANCE, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    objects = ContentConstraintManager()

class ConstraintKeySet(models.Model):
    attachment_constraint = models.ForeignKey(AttachmentConstraint, on_delete=models.CASCADE, related_name='data_key_sets', null=True, blank=True)
    content_constraint = models.ForeignKey(ContentConstraint, on_delete=models.CASCADE, related_name='data_key_sets', null=True, blank=True)

    objects = DataKeySetManager()

    def __str__(self):
        constraint = self.attachment_constraint.id_code if self.attachment_constraint else self.content_constraint.id_code
        return '%s-%s' % (constraint, self.id)

class Key(models.Model):
    constraint_key_set = models.ForeignKey(ConstraintKeySet, null=True, blank=True, related_name='data_keys', on_delete=models.CASCADE)

    objects = ConstraintDataKeyManager()

    def key(self):
        return ', '.join('%s: %s' % pair.get_value() for pair in self.key_values)  

    def __str__(self):
        return self.data_key()

class KeyValue(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, related_name='key_values')
    component_id = models.CharField(max_length=255)
    code_value = models.ForeignKey(Code, null=True, blank=True, on_delete=models.CASCADE)
    string_value = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('key', 'component_id')

    objects = KeyValueManager()

    def get_value(self):
        component = self.component_id 
        value = self.code_value.id_code if self.code_value else self.string_value
        return (component, value)

    def __str__(self):
        return '%s-%s:%s' % (self.constraint_data_key, *self.get_value())

class CubeRegion(models.Model):
    content_constraint = models.ForeignKey(ContentConstraint, on_delete=models.CASCADE, related_name='cube_regions')
    include = models.BooleanField(default=True)

    def region(self):
        return ', '.join('%s: (%s)' % (key_value_set[0][0], ', '.join(key_value_set[1])) for key_value_set in self.key_value_sets) 

    def __str__(self):
        constraint = self.content_constraint.id_code
        return '%s-%s' % (constraint, self.id)

class KeyValueSet(models.Model):
    cube_region = models.ForeignKey(CubeRegion, on_delete=models.CASCADE, related_name='key_value_sets')
    component_id = models.CharField(max_length=255, blank=True)
    code_values = models.ManyToManyField(Code, through='CodeValueDetail')
    string_values = models.CharField(max_length=511, blank=True)
    start_time = models.CharField(max_length=maxlengths.TIME_PERIOD, null=True, blank=True)
    end_time = models.CharField(max_length=maxlengths.TIME_PERIOD, null=True, blank=True)
    start_inclusive = models.NullBooleanField(blank=True)
    end_inclusive = models.NullBooleanField(blank=True)

    class Meta:
        unique_together = ('cube_region', 'component_id')

    def is_dimension(self):
        return True if self.dimension else False

    def is_attribute(self):
        return True if self.attribute else False

    def is_time(self):
        return True if self.start_time or self.end_time else False

    def is_string(self):
        return  True if self.string_values else False

    def is_code(self):
        if not self.is_time and not self.is_string:
            return True
        else:
            return False

    def get_value_set(self):
        component = self.dimension.id_code if self.is_dimension else self.attribute.id_code
        if self.is_time: 
            return ((component, 'time'), (self.start_time, self.start_inclusive), (self.end_time, self.end_inclusive))
        elif self.is_string:
            values = (string.value for string in self.string_values)
            return ((component, 'string'), list(values))
        else:
            values = ((detail.code.id_code, detail.cascade) for detail in self.code_value_details)
            return ((component, 'code'), list(values))

    def __str__(self):
        return self.get_value_set()

class CodeValueDetail(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    key_value_set = models.ForeignKey(KeyValueSet, on_delete=models.CASCADE, related_name='code_value_details')
    cascade = models.BooleanField(default=False)

    objects = CodeValueDetailManager()

    def __str__(self):
        return '%s, cascade: %s' % (self.code.id_code, self.cascade)

# from django.db import models
#
# from .abstract_postorg import MaintainableArtefact 
# from .codelist import Code
# from .data import DataDimensionString, TimeValue, MetadataDataAttributeValue 
# from .data_structly import Dataflow, DataStructure, Datasource, Dimension, Attribute
# from .metadata_structly import Report, MetadataAttribute, MetadataStructure, Metadataflow, MetadataTargetComponent, MetadataTarget
# from .organisation import Organisation
# from .provision import DataProvisionAgreement, MetadataProvisionAgreement
# from .reference import ReferenceObject
# from .registration import Dataset
#
# from ..managers.constraint import (
#     ConstraintDataKeyManager, KeyValueManager, CodeValueDetailManager,
#     AttachmentConstraintManager, ContentConstraintManager, DataKeySetManager,
#     MetadataKeySetManager, MetadataKeyValueManager
# )
# from ..settings import api_maxlen_settings
#
# class Constraint(MaintainableArtefact):
#     attached2datasets = models.ManyToManyField(Dataset)
#     attached2datasources = models.ManyToManyField(Datasource)
#     attached2provisions = models.ManyToManyField(DataProvisionAgreement)
#
#     class Meta(MaintainableArtefact.Meta):
#         abstract = True
#
#     def attached2ids(self, attachset):
#         return (attach.id_code for attach in self.get(attachset))
#
#     def provisions(self):
#         return self.attached2ids('attached2provisions')
#
# class AttachmentConstraint(Constraint):
#     attached2dsds = models.ManyToManyField(DataStructure, related_name='attachemt_constraints')
#     attached2dataflows = models.ManyToManyField(Dataflow, related_name='attachment_constraints')
#
#     objects = AttachmentConstraintManager()
#
#     def dsds(self):
#         return self.attached2ids('attached2dsds')
#     def dataflows(self):
#         return self.attached2ids('attached2dataflows')
#     def datasources(self):
#         return self.attached2ids('attached2datasources')
#     def datasets(self):
#         return self.attached2ids('attached2dataset')
#
# class ContentConstraint(Constraint):
#     attached2dataproviders = models.ManyToManyField(Organisation, related_name='content_constraints')
#     attached2dsds = models.ManyToManyField(DataStructure, related_name='content_constraints')
#     attached2dataflows = models.ManyToManyField(Dataflow, related_name='content_constraints')
#     attached2datasets = None 
#     attached2datasources = None
#     attached2dataset = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE) 
#     attached2datasource = models.ForeignKey(Datasource, null=True, blank=True, on_delete=models.CASCADE) 
#     periodicity = models.CharField(max_length=api_maxlen_settings.PERIODICITY, null=True, blank=True)
#     offset = models.CharField(max_length=api_maxlen_settings.OFFSET, null=True, blank=True)
#     tolerance = models.CharField(max_length=api_maxlen_settings.TOLERANCE, null=True, blank=True)
#     start_time = models.DateTimeField(null=True, blank=True)
#     end_time = models.DateTimeField(null=True, blank=True)
#
#     objects = ContentConstraintManager()
#
# class DataKeySet(models.Model):
#     attachment_constraint = models.ForeignKey(AttachmentConstraint, on_delete=models.CASCADE, related_name='data_key_sets')
#     content_constraint = models.ForeignKey(ContentConstraint, on_delete=models.CASCADE, related_name='data_key_sets')
#
#     objects = DataKeySetManager()
#
#     def __str__(self):
#         constraint = self.attachment_constraint.id_code if self.attachment_constraint else self.content_constraint.id_code
#         return '%s-%s' % (constraint, self.id)
#
# class ConstraintDataKey(models.Model):
#     data_key_set = models.ForeignKey(DataKeySet, on_delete=models.CASCADE, related_name='data_keys')
#
#     objects = ConstraintDataKeyManager()
#
#     def data_key(self):
#         return ', '.join('%s: %s' % pair.get_value() for pair in self.key_values)  
#
#     def __str__(self):
#         return self.data_key()
#
# class KeyValue(models.Model):
#     constraint_data_key = models.ForeignKey(ConstraintDataKey, on_delete=models.CASCADE, related_name='key_values')
#     # In the following the dimension is linked to a specific dimension of
#     # a DSD.  We are not though interested on that specific DSD.  We are
#     # interested only at the id_code of the dimension, since a constraint
#     # can be attached to many dataflows or DSDs that have a dimension with
#     # identical identifier.
#     dimension = models.ForeignKey(Dimension, null=True, blank=True, on_delete=models.CASCADE)
#     #attribute = models.ForeignKey(Attribute, null=True, blank=True, on_delete=models.CASCADE)
#     code_value = models.ForeignKey(Code, null=True, blank=True, on_delete=models.CASCADE)
#     string_value = models.ForeignKey(DataDimensionString, null=True, blank=True, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('data_key', 'dimension')
#
#     objects = KeyValueManager()
#
#     def get_value(self):
#         component = self.dimension.id_code if self.dimension else self.attribute.id_code
#         value = self.code_value.id_code if self.code_value else self.string_value.value
#         return (component, value)
#
#     def __str__(self):
#         return '%s-%s:%s' % (self.constraint_data_key, *self.get_value())
#
# class CubeRegion(models.Model):
#     content_constraint = models.ForeignKey(ContentConstraint, on_delete=models.CASCADE, related_name='cube_regions')
#     include = models.BooleanField(default=True)
#
#     def region(self):
#         return ', '.join('%s: (%s)' % (key_value_set[0][0], ', '.join(key_value_set[1])) for key_value_set in self.key_value_sets) 
#
#     def __str__(self):
#         constraint = self.content_constraint.id_code
#         return '%s-%s' % (constraint, self.id)
#
# class KeyValueSet(models.Model):
#     cube_region = models.ForeignKey(CubeRegion, on_delete=models.CASCADE, related_name='key_value_sets')
#     # In the following the dimension is linked to a specific dimension of
#     # a DSD.  We are not though interested on that specific DSD.  We are
#     # interested only at the id_code of the dimension, since a constraint
#     # can be attached to many dataflows or DSDs that have a dimension with
#     # identical identifier.
#     dimension = models.ForeignKey(Dimension)
#     attribute = models.ForeignKey(Attribute)
#     code_values = models.ManyToManyField(Code, through='CodeValueDetail')
#     string_values = models.ManyToManyField(DataDimensionString)
#     start_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     end_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     start_inclusive = models.NullBooleanField(blank=True)
#     end_inclusive = models.NullBooleanField(blank=True)
#
#     class Meta:
#         unique_together = ('cube_region', 'dimension', 'attribute')
#     
#     def is_dimension(self):
#         return True if self.dimension else False
#
#     def is_attribute(self):
#         return True if self.attribute else False
#
#     def is_time(self):
#         return True if self.start_time or self.end_time else False
#         
#     def is_string(self):
#         return  True if self.string_values else False
#
#     def is_code(self):
#         if not self.is_time and not self.is_string:
#             return True
#         else:
#             return False
#
#     def get_value_set(self):
#         component = self.dimension.id_code if self.is_dimension else self.attribute.id_code
#         if self.is_time: 
#             return ((component, 'time'), (self.start_time, self.start_inclusive), (self.end_time, self.end_inclusive))
#         elif self.is_string:
#             values = (string.value for string in self.string_values)
#             return ((component, 'string'), list(values))
#         else:
#             values = ((detail.code.id_code, detail.cascade) for detail in self.code_value_details)
#             return ((component, 'code'), list(values))
#             
#     def __str__(self):
#         return self.get_value_set()
#
# class CodeValueDetail(models.Model):
#     code = models.ForeignKey(Code, on_delete=models.CASCADE)
#     key_value_set = models.ForeignKey(KeyValueSet, on_delete=models.CASCADE, related_name='code_value_details')
#     cascade = models.BooleanField(default=False)
#
#     objects = CodeValueDetailManager()
#
#     def __str__(self):
#         return '%s, cascade: %s' % (self.code.id_code, self.cascade)
#
# class MetaConstraint(MaintainableArtefact):
#     attached2metadsds = models.ManyToManyField(MetadataStructure, related_name='attachment_constraints')
#     attached2metadataflows = models.ManyToManyField(Metadataflow, related_name='attachment_constraints')
#     attached2datasets = models.ManyToManyField(Dataset) 
#     attached2datasources = models.ManyToManyField(Datasource)
#     attached2metaprovision = models.ManyToManyField(MetadataProvisionAgreement) 
#
#     class Meta(MaintainableArtefact.Meta):
#         abstract = True
#
# class MetaattachmentConstraint(MetaConstraint):
#     pass
#
# class MetacontentConstraint(MetaConstraint):
#     attached2dataproviders = models.ManyToManyField(Organisation, related_name='content_constraints')
#     attached2metadsds = models.ManyToManyField(MetadataStructure, related_name='content_constraints')
#     attached2metadataflows = models.ManyToManyField(Metadataflow, related_name='content_constraints')
#     attached2datasets = None 
#     attached2datasources = None
#     attached2dataset = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE) 
#     attached2datasource = models.ForeignKey(Datasource, null=True, blank=True, on_delete=models.CASCADE) 
#     periodicity = models.CharField(max_length=api_maxlen_settings.PERIODICITY, null=True, blank=True)
#     offset = models.CharField(max_length=api_maxlen_settings.OFFSET, null=True, blank=True)
#     tolerance = models.CharField(max_length=api_maxlen_settings.TOLERANCE, null=True, blank=True)
#     start_time = models.DateTimeField(null=True, blank=True)
#     end_time = models.DateTimeField(null=True, blank=True)
#
# class MetadataKeySet(models.Model):
#     metaattachment_constraint = models.ForeignKey(MetaattachmentConstraint, on_delete=models.CASCADE, related_name='metadata_key_sets')
#     metacontent_constraint = models.ForeignKey(MetacontentConstraint, on_delete=models.CASCADE, related_name='metadata_key_sets')
#
#     objects = MetadataKeySetManager()
#
#     def __str__(self):
#         metaconstraint = self.metaattachment_constraint.id_code if self.metaattachment_constraint else self.metacontent_constraint.id_code
#         return '%s-%s' % (metaconstraint, self.id)
#
# class MetadataKey(models.Model):
#     metadata_key_set = models.ForeignKey(MetadataKeySet, on_delete=models.CASCADE, related_name='metadata_keys')
#     target = models.ForeignKey(MetadataTarget)
#     report = models.ForeignKey(Report)
#
#     objects = MetadataKeySetManager()
#
#     # def data_key(self):
#     #     return ', '.join('%s: %s' % pair.get_value() for pair in self.key_values)  
#
#     # def __str__(self):
#     #     return self.data_key()
#
# class MetadataKeyValue(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     target_component = models.ForeignKey(MetadataTargetComponent)
#     value = models.ForeignKey(TimeValue, null=True, blank=True, on_delete=models.CASCADE)
#     dataset = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE)
#     data_key = models.ForeignKey('DataAnyKey', null=True, blank=True, on_delete=models.CASCADE)
#     objekt = models.ForeignKey(ReferenceObject, null=True, blank=True)
#
#     class Meta:
#         unique_together = (
#             'metadata_key', 'target_component', 'value', 'data_set',
#             'data_key', 'objekt' 
#         )
#
#     objects = MetadataKeyValueManager()
#
#     def get_value(self):
#         component = self.target_component.id_code 
#         if self.value:
#             value = self.value.value
#         elif self.dataset: 
#             value = self.dataset.set_id
#
#         return (component, value)
#
#     def __str__(self):
#         return '%s-%s:%s' % (self.constraint_data_key, *self.get_value())
#     
# class MetadataTargetRegion(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     constraint = models.ForeignKey(MetacontentConstraint, on_delete=models.CASCADE, related_name='metadata_target_regions')
#     target = models.ForeignKey(MetadataTarget)
#     report = models.ForeignKey(Report)
#
# class MetadataKeyValueSet(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     metadata_target_region = models.ForeignKey(MetadataTargetRegion, on_delete=models.CASCADE, related_name='metakey_value_sets')
#     target_component = models.ForeignKey(MetadataTargetComponent)
#     values = models.ManyToManyField('TimeValue')
#     data_sets = models.ManyToManyField(Dataset)
#     data_keys = models.ManyToManyField('DataAnyKey')
#     objekts = models.ManyToManyField(ReferenceObject) 
#     start_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     end_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     start_inclusive = models.NullBooleanField(null=True, blank=True)
#     end_inclusive = models.NullBooleanField(null=True, blank=True)
#
# class MetadataAttrValueSet(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     metadata_target_region = models.ForeignKey(MetadataTargetRegion, on_delete=models.CASCADE, related_name='metaattr_value_sets')
#     attribute = models.ForeignKey(MetadataAttribute)
#     values = models.ManyToManyField(MetadataDataAttributeValue)
#     cascade = models.BooleanField(default=False) 
#     start_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     end_time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
#     start_inclusive = models.NullBooleanField(blank=True, null=True)
#     end_inclusive = models.NullBooleanField(blank=True, null=True)
#
# class DataAnyKey(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     dataflow = models.ForeignKey(Dataflow)
#
# class DataAnyKeyValue(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     data_any_key = models.ForeignKey(DataAnyKey, on_delete=models.CASCADE, related_name = 'dim_values')
#     dimension = models.ForeignKey(Dimension)
#     code_value = models.ForeignKey(Code, null=True, blank=True, on_delete=models.CASCADE)
#     string_value = models.ForeignKey(DataDimensionString, null=True, blank=True, on_delete=models.CASCADE)
#
# class TimeValue(models.Model):
#     metadata_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE, related_name='metakey_values')
#     time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
