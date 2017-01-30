from django.db import models
from . import enum

class RefBase(models.Model):
    agencyID = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    maintainableParentID = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    maintainableParentVersion = models.CharField(max_length=enum.max_length['id'], null=True, blank=True, default = '1.0')
    containerID = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    id_ = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    version = models.CharField(max_length=enum.max_length['id'], null=True, blank=True, default = '1.0')
    local = models.BooleanField(null=True, blank=True)
    class_ = models.CharField(max_length=enum.max_length['id'], choices = enum.class_types)
    package = models.CharField(max_length=enum.max_length['id'], choices = enum.package_types)

class Reference(models.Model):
    Ref = models.ForeignKey(RefBase, on_delete=models.CASCADE, null=True, blank=True)
    URN = models.URLField(null=True, blank=True)

class ISOConceptReference(models.Model):
    ConceptAgency = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    ConceptSchemeID= models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    ConceptID= models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
