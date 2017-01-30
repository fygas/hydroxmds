from django.db import models
from .structure_base import MaintainableArtefact, IdentifiableArtefact
from common.models import Reference
from hvad.models import TranslatedFields
from . import enum
from .top import Representation

class MetadataStructure(MaintainableArtefact):
    MetadataStructureComponents = models.ForeignKey('MetadataStructureComponents', null=True, blank=True)
    translations = TranslatedFields()

class MetadataStructureComponents(models.Model):
    MetadataTargets = models.ManyToManyField('MetadataTargetList', on_delete=models.CASCADE, null=True, blank=True)
    ReportStructures = models.ManyToManyField('ReportStructureList', on_delete=models.CASCADE, null=True, blank=True)

class MetadataTargetList(IdentifiableArtefact):
    MetadataTargetList = models.ManyToManyField('MetadataTarget', on_delete=models.CASCADE, null=True, blank=True)

class ReportStructureList(IdentifiableArtefact):
    ReportStructureList = models.ManyToManyField('ReportStructure', on_delete=models.CASCADE, null=True, blank=True)

class MetadataTarget(IdentifiableArtefact):
    metadataTarget_type = models.CharField(max_length=enum.max_length['id'], choices = enum.metadataTarget_types, null=True, blank=True)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
    objectType = models.CharField(max_length=enum.max_length['id'], choices = enum.object_types, null=True, blank=True)

class ReportStructure(IdentifiableArtefact):
    minOccurs = models.IntegerField(null=True, blank=True)
    maxOccurs = models.IntegerField(null=True, blank=True)
    isPresentational = models.BooleanField(null=True, blank=True)
    MetadataTargets = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    MetadataAttributes = models.ManyToManyField('self', on_delete=models.CASCADE, null=True, blank=True)
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
