from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from . import constants 

# Concrete Annotation
class Annotation(TranslatableModel):
    urn = models.URLField(null=True, blank=True)
    uri = models.URLField(null=True, blank=True)
    AnnotationTitle = models.CharField(max_length=constants.max_length['name'], null=True, blank=True)
    AnnotationType = models.CharField(max_length=constants.max_length['name'], null=True, blank=True)
    AnnotationURL = models.URLField(null=True, blank=True)
    tranaslations = TranslatedFields(
        AnnotationText = models.TextField(null=True, blank=True)
    )
    id_code = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)

# Abstract models
class AnnotableArtefact(TranslatableModel):
    class Meta:
        abstract = True
    Annotations = models.ManyToManyField(Annotation, related_name='+')

# Concrete models 
class RefBase(models.Model):
    agencyID = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    maintainableParentID = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    maintainableParentVersion = models.CharField(max_length=constants.max_length['id'], null=True, blank=True, default = '1.0')
    containerID = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    id_code = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    version = models.CharField(max_length=constants.max_length['id'], null=True, blank=True, default = '1.0')
    local = models.NullBooleanField(null=True, blank=True)
    class_code = models.CharField(max_length=constants.max_length['id'], choices = constants.class_types)
    package = models.CharField(max_length=constants.max_length['id'], choices = constants.package_types)

class Reference(models.Model):
    Ref = models.ForeignKey(RefBase, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    URN = models.URLField(null=True, blank=True)

class ISOConceptReference(models.Model):
    ConceptAgency = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    ConceptSchemeID= models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    ConceptID= models.CharField(max_length=constants.max_length['id'], null=True, blank=True)


class Text(TranslatableModel):
    tranaslations = TranslatedFields(
        Text = models.TextField(null=True, blank=True)
    )

class Key(models.Model):
    KeyValues = models.ManyToManyField('ComponentValueSet', blank=True, related_name='+')
    Attributes = models.ManyToManyField('ComponentValueSet', blank=True, related_name='+')
    include = models.NullBooleanField(null=True, blank=True, default=True)

class ComponentValueSet(models.Model):
    Values = models.ManyToManyField('SimpleValue', blank=True, related_name='+') 
    DataSet = models.ManyToManyField(Reference, blank=True, related_name='+')
    DataKey = models.ManyToManyField(Key, blank=True, related_name='+')
    Object = models.ManyToManyField(Reference, blank=True, related_name='+')
    TimeRange = models.ForeignKey('TimeRangeValue', null=True, blank=True, related_name='+')
    idc = models.CharField(max_length=constants.max_length['id'], null=True, blank=True)
    include = models.NullBooleanField(null=True, blank=True, default=True)

class SimpleValue(models.Model):
    value = models.CharField(max_length=constants.max_length['id'])
    cascadeValues = models.NullBooleanField(null=True, blank=True)

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
    isRESTDatasource = models.NullBooleanField(blank=True)
    isWebServiceDatasource = models.NullBooleanField(blank=True)
