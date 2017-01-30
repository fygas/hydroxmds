from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from . import enum
from .common_references import Reference

# Abstract models
class AnnotableArtefact(TranslatableModel):
    class Meta:
        abstract = True
    Annotations = models.ManyToManyField('Annotation', on_delete=models.CASCADE, null=True, blank=True)

# Concrete models 
class Annotation(TranslatableModel):
    urn = models.URLField(null=True, blank=True)
    uri = models.URLField(null=True, blank=True)
    AnnotationTitle = models.CharField(max_length=enum.max_length['name'], null=True, blank=True)
    AnnotationType = models.CharField(max_length=enum.max_length['name'], null=True, blank=True)
    AnnotationURL = models.URLField(null=True, blank=True)
    tranaslations = TranslatedFields(
        AnnotationText = models.TextField(null=True, blank=True)
    )
    id_ = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)


class Text(TranslatableModel):
    tranaslations = TranslatedFields(
        Text = models.TextField(null=True, blank=True)
    )

class TextFormat(models.Model):
    textType = models.CharField(max_length=enum.max_length['DataType'], null=True, blank=True, default='String', choices=enum.data_types)
    isSequence = models.BooleanField(null=True, blank=True)
    interval = models.DecimalField(null=True, blank=True)
    startValue = models.DecimalField(null=True, blank=True)
    endValue = models.DecimalField(null=True, blank=True)
    timeInterval = models.DurationField(null=True, blank=True)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    minLength = models.PositiveIntegerField(null=True, blank=True)
    maxLength = models.PositiveIntegerField(null=True, blank=True)
    minValue= models.DecimalField(null=True, blank=True)
    maxValue = models.DecimalField(null=True, blank=True)
    decimals = models.PositiveIntegerField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    isMultiLingual = models.BooleanField(null=True, blank=True, default=True)

class Key(models.Model):
    KeyValues = models.ManyToManyField('ComponentValueSet', on_delete=models.CASCADE, null=True, blank=True)
    Attributes = models.ManyToManyField('ComponentValueSet', on_delete=models.CASCADE, null=True, blank=True)
    include = models.BooleanField(null=True, blank=True, default=True)

class ComponentValueSet(models.Model):
    Values = models.ManyToManyField('SimpleValue', on_delete=models.CASCADE, null=True, blank=True) 
    DataSet = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    DataKey = models.ManyToManyField 
    Object = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    TimeRange = models.ForeignKey('TimeRangeValue', on_delete=models.CASCADE, null=True, blank=True)
    id_ = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    include = models.BooleanField(null=True, blank=True, default=True)

class SimpleValue(models.Model):
    value = models.CharField(max_length=enum.max_length['id'])
    cascadeValues = models.BooleanField(null=True, blank=True, default=False)

class TimeRangeValue(models.Model):
    #Simplified this and assumed that dates are inclusive
    BeforePeriod = models.DateTimeField(null=True, blank=True)
    AfterPeriod = models.DateTimeField(null=True, blank=True)
    StartPeriod = models.DateTimeField(null=True, blank=True)
    EndPeriod = models.DateTimeField(null=True, blank=True)

class QueryableDataSource(models.Model):
    DataURL = models.URLField(null=True, blank=True)
    WSDLURL = models.URLField(null=True, blank=True)
    WADLURL = models.URLField(null=True, blank=True)
    isRESTDatasource = models.BooleanField(null=True, blank=True)
    isWebServiceDatasource = models.BooleanField(null=True, blank=True)
