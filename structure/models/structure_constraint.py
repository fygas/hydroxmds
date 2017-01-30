from . import enum
from django.db import models
from .structure_base import MaintainableArtefact 
from common.models import Reference, Key, QueryableDataSource
from hvad.models import TranslatedFields

#Constraint Structure - check which models to move
class ConstraintArtefact(MaintainableArtefact):
    type_ = models.CharField(max_length=enum.max_length['id'], choices=enum.Constraint_types, null=True, blank=True)
    ConstraintAttachment = models.ForeignKey('ConstraintAttachment', on_delete=models.CASCADE, null=True, blank=True)
    DataKeySet = models.ManyToManyField('KeySet', on_delete=models.CASCADE, null=True, blank=True)
    MetadataKeySet = models.ManyToManyField('KeySet', on_delete=models.CASCADE, null=True, blank=True)
    CubeRegion = models.ManyToManyField(Key, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class KeySet(models.Model):
    Keys = models.ManyToManyField(Key, on_delete=models.CASCADE, null=True, blank=True)
    isIncluded = models.BooleanField(null=True, blank=True)

class ConstraintAttachment(models.Model):
    DataProvider = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    DataSet = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    MetadataSet = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    SimpleDataSource = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    DataStructure = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    MetadataStructure = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Dataflow = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Metadataflow = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    ProvisionAgreement = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    QueryableDataSource= models.ManyToManyField(QueryableDataSource, on_delete=models.CASCADE, null=True, blank=True)

