from django.db import models
from .structure_base import MaintainableArtefact, IdentifiableArtefact
from common.models import Reference
from hvad.models import TranslatedFields
from common.models.constants import max_length
from .constants import metadataTarget_types, object_types
from .structure import Representation

class MetadataStructure(MaintainableArtefact):
    MetadataStructureComponents = models.ForeignKey('MetadataStructureComponents', null=True, blank=True)
    translations = TranslatedFields()

class MetadataStructureComponents(models.Model):
    MetadataTargets = models.ManyToManyField('MetadataTargetList', null=True, blank=True)
    ReportStructures = models.ManyToManyField('ReportStructureList', null=True, blank=True)

class MetadataTargetList(IdentifiableArtefact):
    MetadataTargetList = models.ManyToManyField('MetadataTarget', null=True, blank=True)
    translations = TranslatedFields()

class ReportStructureList(IdentifiableArtefact):
    ReportStructureList = models.ManyToManyField('ReportStructure', null=True, blank=True)
    translations = TranslatedFields()

class MetadataTarget(IdentifiableArtefact):
    metadataTarget_type = models.CharField(max_length=max_length['id'], choices = metadataTarget_types, null=True, blank=True)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
    objectType = models.CharField(max_length=max_length['id'], choices = object_types, null=True, blank=True)
    translations = TranslatedFields()

class ReportStructure(IdentifiableArtefact):
    minOccurs = models.IntegerField(null=True, blank=True)
    maxOccurs = models.IntegerField(null=True, blank=True)
    isPresentational = models.BooleanField(null=True, blank=True)
    MetadataTargets = models.ManyToManyField(Reference, null=True, blank=True)
    MetadataAttributes = models.ManyToManyField('self', null=True, blank=True)
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
