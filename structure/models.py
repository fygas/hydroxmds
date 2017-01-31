from django.db import models
from hvad.models import TranslatedFields

from common.constants import max_length, data_types
from common.models import AnnotableArtefact, Reference 

from .constants import dimension_types, object_types

# Abstract models
class IdentifiableArtefact(AnnotableArtefact):
    class Meta:
        abstract = True
    urn = models.URLField(null=True, blank=True)
    uri = models.URLField(null=True, blank=True)
    id_code = models.CharField(max_length=max_length['id'], null=True, blank=True)

class NameableArtefact(IdentifiableArtefact):
    class Meta:
        abstract = True
    tranaslations = TranslatedFields(
        Name = models.CharField(max_length=max_length['id'], null=True, blank=True),
        Description = models.TextField(null=True, blank=True)
    )

class VersionableArtefact(NameableArtefact):
    class Meta:
        abstract = True
    version = models.CharField(max_length=max_length['id'], null=True, blank=True)
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo = models.DateTimeField(null=True, blank=True)

class MaintainableArtefact(VersionableArtefact):
    class Meta:
        abstract = True
    agencyID = models.CharField(max_length=max_length['id'], null=True, blank=True)
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
class TextFormatInfo(models.Model):
    textType = models.CharField(max_length=max_length['id'], null=True, blank=True, choices=data_types)
    isSequence = models.NullBooleanField(null=True, blank=True)
    interval = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    startValue = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    endValue = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    timeInterval = models.DurationField(null=True, blank=True)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    minLength = models.PositiveIntegerField(null=True, blank=True)
    maxLength = models.PositiveIntegerField(null=True, blank=True)
    minValue= models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    maxValue = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    decimals = models.PositiveIntegerField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    isMultiLingual = models.NullBooleanField(null=True, blank=True)

class Representation(models.Model):
    TextFormat = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Enumeration = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    EnumerationFormat = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')

class ComponentList(IdentifiableArtefact):
    Components = models.ManyToManyField('Component', related_name='+')
    translations = TranslatedFields()

class Component(IdentifiableArtefact):
    position = models.PositiveIntegerField(null=True, blank=True)
    dimension_type = models.CharField(max_length=max_length['id'], choices = dimension_types, null=True, blank=True)
    objectType = models.CharField(max_length=max_length['id'], choices = object_types, null=True, blank=True)
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    ConceptRole= models.ManyToManyField(Reference, related_name='+')
    GroupDimensions = models.ManyToManyField(Reference, related_name='+')
    AttachmentConstraint = models.ManyToManyField(Reference, related_name='+')
    translations = TranslatedFields()
