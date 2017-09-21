from django.db import models

from common.constants import max_length

from ..models import MaintainableArtefact 
from common.models import Reference, Key, QueryableDataSource

class DataStructureConstraint(MaintainableArtefact):
    dsds = models.ManyToManyField(DataStructureConstraint)
#Constraint Structure - check which models to move
# class ConstraintArtefact(MaintainableArtefact):
#     type_code = models.CharField(max_length=max_length['id'], null=True, blank=True, choices=Constraint_types)
#     ConstraintAttachment = models.ForeignKey('ConstraintAttachment', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
#     DataKeySet = models.ManyToManyField('KeySet', related_name='+')
#     MetadataKeySet = models.ManyToManyField('KeySet', related_name='+')
#     CubeRegion = models.ManyToManyField(Key, related_name='+')
#     translations = TranslatedFields()
#
# class KeySet(models.Model):
#     Keys = models.ManyToManyField(Key, related_name='+')
#     isIncluded = models.NullBooleanField(null=True, blank=True)
#
# class ConstraintAttachment(models.Model):
#     DataProvider = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
#     DataSet = models.ManyToManyField(Reference, related_name='+')
#     MetadataSet = models.ManyToManyField(Reference, related_name='+')
#     SimpleDataSource = models.ManyToManyField(Reference, related_name='+')
#     DataStructure = models.ManyToManyField(Reference, related_name='+')
#     MetadataStructure = models.ManyToManyField(Reference, related_name='+')
#     Dataflow = models.ManyToManyField(Reference, related_name='+')
#     Metadataflow = models.ManyToManyField(Reference, related_name='+')
#     ProvisionAgreement = models.ManyToManyField(Reference, related_name='+')
#     QueryableDataSource= models.ManyToManyField(QueryableDataSource, related_name='+')
