from django.db import models

from .codelist import Code
from .conceptscheme import Concept
from .constraint import AttachmentConstraint, DataAnyKey 
from .data_structly import Dataflow, Dimension, Attribute
from .metadata_structly import MetadataFlow, MetadataTargetComponent, MetadataTarget, Report
from .reference import ReferenceObject
from .registration import Dataset, Metadataset

from ..constants import ACTIONS
from ..settings import api_maxlen_settings 
from ..validators import clean_validators

class DataKeyBase(models.model):
    registrations = models.ManyToManyField(Dataset, editable=False, related_name='+')
    attached_attrs = models.ManyToManyField('AttrValue')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not kwargs.get('registration'):
            created = not bool(self.pk)
            action = 'Append' if created else 'Replace'
            from ..utils.permissions import get_current_user
            created_by = get_current_user()
            kwargs['registration'] = Dataset(created_by=created_by, action=action, interactive=True).save()
        self.registrations.add(kwargs.pop('registration'))
        super().save(*args, **kwargs)

    def delete(self):
        action = 'Delete'
        from ..utils.permissions import get_current_user
        created_by = get_current_user()
        Dataset(created_by=created_by, action=action).save()
        super().delete()

class DataPartialKey(DataKeyBase):
    dataflow = models.ForeignKey(Dataflow)

class DataPartialKeyValue(models.Model):
    data_partial_key = models.ForeignKey(DataPartialKey, on_delete=models.CASCADE, related_name = 'dim_values')
    dimension = models.ForeignKey(Dimension)
    code_value = models.ForeignKey(Code, on_delete=models.CASCADE)
    string_value = models.ForeignKey('StringDataDimension', null=True, blank=True, on_delete=models.CASCADE)

class DataMeasureKey(DataKeyBase):
    data_partial_key = models.ForeignKey(DataPartialKey, on_delete=models.CASCADE)
    measure_value = models.ForeignKey(Concept, null=True, blank=True, on_delete=models.CASCADE)

class DataKey(DataKeyBase):
    data_measure_key = models.ForeignKey(DataMeasureKey, on_delete=models.CASCADE, null=True, blank=True)
    time_value = models.ForeignKey('TimeValue', null=True, blank=True, on_delete=models.CASCADE)

class AttrValue(models.Model):
    annotations = None
    attribute = models.ForeignKey(Attribute)
    code_value = models.ForeignKey(Code)
    string_value = models.CharField(max_length=api_maxlen_settings.DATA_ATTRIBUTE, null=True, blank=True)

class Obs(models.Model):
    data_key = models.ForeignKey(DataKey, on_delete=models.CASCADE)
    value = models.CharField(max_length=api_maxlen_settings.OBS_VALUE)
    registration = models.ForeignKey(Dataset, on_delete=models.CASCADE, editable=False, related_name='+')
    action = models.CharField(min_length=api_maxlen_settings.ACTIONS, choices=ACTIONS)

    def clean(self):
        created = not bool(self.pk)
        if not created:
            raise clean_validators[self.__class__.__name__] 

    def delete(self):
        action = 'Delete'
        from ..utils.permissions import get_current_user
        created_by = get_current_user()
        Dataset(created_by=created_by, action=action).save()
        super().delete()

class MetadataDataTarget(models.Model):
    metadata_flow = models.ForeignKey(MetadataFlow)
    target = models.ForeignKey(MetadataTarget)
    report = models.ForeignKey(Report)

class MetadataDataTargetValue(models.Model):
    metadata_data_target = models.ForeignKey(MetadataDataTarget, on_delete=models.CASCADE, related_name='component_values')
    component = models.ForeignKey(MetadataTargetComponent)
    value = models.CharField('TimeValue')
    data_set = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE)
    data_key = models.ManyToManyField(DataAnyKey, null=True, blank=True, on_delete=models.CASCADE)
    constraint_value = models.ForeignKey(AttachmentConstraint, null=True, blank=True, on_delete=models.CASCADE)
    objekt = models.ForeignKey(ReferenceObject, null=True, blank=True, on_delete=models.CASCADE)

class MetadataDataAttributeValue(models.Model):
    code_value = models.ForeignKey(Code, on_delete=models.CASCADE, null=True, blank=True)
    string_value = models.ForeignKey('MetadataDataAttributeString', on_delete=models.CASCADE, null=True, blank=True)

class MetadataDataAttribute(models.Model):
    metadata_data_target = models.ForeignKey(MetadataDataTarget, on_delete=models.CASCADE, related_name='component_values')
    attribute = models.ForeignKey('MetadataAttribute')
    values = models.ManyToManyField(MetadataDataAttributeValue, through='MetadataDataAttributeOrderedValue')

class MetadataDataAttributeOrderedValue(models.Model):
    value = models.ForeignKey(MetadataDataAttributeValue)
    group = models.ForeignKey(MetadataDataAttribute)
    order = models.IntegerField(default=0)
    registration = models.ForeignKey(Metadataset, on_delete=models.CASCADE)

### Common String Models
class MetadataDataAttributeString(models.Model):
    value = models.TextField()

class StringDataDimension(models.Model):
    value = models.CharField(max_length=api_maxlen_settings.DATA_DIMENSION, blank=True)

class TimeValue(models.Model):
    time = models.CharField(max_length=api_maxlen_settings.TIME_PERIOD, null=True, blank=True)
