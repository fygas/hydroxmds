from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from . import enum
from .structure import Representation
from common.models import AnnotableArtefact, Reference

# Abstract models
class IdentifiableArtefact(AnnotableArtefact):
    class Meta:
        abstract = True
    urn = models.URLField(null=True, blank=True)
    uri = models.URLField(null=True, blank=True)
    id_ = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)

class NameableArtefact(TranslatableModel, IdentifiableArtefact):
    class Meta:
        abstract = True
    tranaslations = TranslatedFields(
        Name = models.CharField(max_length=enum.max_length['id'], null=True, blank=True),
        Description = models.TextField(null=True, blank=True)
    )

class VersionableArtefact(NameableArtefact):
    class Meta:
        abstract = True
    version = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo = models.DateTimeField(null=True, blank=True)

class MaintainableArtefact(VersionableArtefact):
    class Meta:
        abstract = True
    agencyID = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    isFinal = models.BooleanField(default=False)
    isExternalReference= models.BooleanField(default=False)

class ItemScheme(MaintainableArtefact):
    class Meta:
        abstract = True
    isPartial = models.BooleanField(default=False)

class Item(NameableArtefact):
    class Meta:
        abstract = True

class ItemSchemeMap(MaintainableArtefact):
    class Meta:
        abstract = True
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)

class ItemAssociation(ItemSchemeMap):
    class Meta:
        abstract = True

#Concrete models
class ComponentList(IdentifiableArtefact):
    Components = models.ManyToManyField('Component', on_delete=models.CASCADE, null=True, blank=True)

class Component(IdentifiableArtefact):
    position = models.PositiveIntegerField(null=True, blank=True)
    dimension_type = models.CharField(max_length=enum.max_length['id'], choices = enum.dimension_types, null=True, blank=True)
    objectType = models.CharField(max_length=enum.max_length['id'], choices = enum.object_types, null=True, blank=True)
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
    ConceptRole= models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    GroupDimensions = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    AttachmentConstraint = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
