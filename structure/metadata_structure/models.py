from django.db import models
from hvad.models import TranslatedFields

from ..constants import metadataTarget_types, object_types
from common.constants import max_length

from ..models import MaintainableArtefact, IdentifiableArtefact, Representation
from common.models import Reference

class MetadataStructure(MaintainableArtefact):
    MetadataStructureComponents = models.ForeignKey('MetadataStructureComponents', null=True, blank=True, related_name='+')
    translations = TranslatedFields()

class MetadataStructureComponents(models.Model):
    MetadataTargets = models.ManyToManyField('MetadataTargetList', related_name='+')
    ReportStructures = models.ManyToManyField('ReportStructureList', related_name='+')

class MetadataTargetList(IdentifiableArtefact):
    MetadataTargetList = models.ManyToManyField('MetadataTarget', related_name='+')
    translations = TranslatedFields()

class ReportStructureList(IdentifiableArtefact):
    ReportStructureList = models.ManyToManyField('ReportStructure', related_name='+')
    translations = TranslatedFields()

class MetadataTarget(IdentifiableArtefact):
    metadataTarget_type = models.CharField(max_length=max_length['id'], null=True, blank=True, choices = metadataTarget_types)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    objectType = models.CharField(max_length=max_length['id'], null=True, blank=True, choices = object_types)
    translations = TranslatedFields()

class ReportStructure(IdentifiableArtefact):
    minOccurs = models.IntegerField(null=True, blank=True)
    maxOccurs = models.IntegerField(null=True, blank=True)
    isPresentational = models.NullBooleanField(null=True, blank=True)
    MetadataTargets = models.ManyToManyField(Reference, related_name='+')
    MetadataAttributes = models.ManyToManyField('self')
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    translations = TranslatedFields()
