from django.conf import settings
from django.db import models
from hvad.models import TranslatedFields

from common.constants import data_types
from common.models import AnnotableArtefact, Reference 
from common.validators import re_validators 

from .constants import dimension_types, object_types

# Abstract models
class IdentifiableArtefact(AnnotableArtefact):
    #urn = models.URLField(null=True, blank=True)
    uri = models.URLField(null=True, blank=True)
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        null=True, blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.id_code

class NameableArtefact(IdentifiableArtefact):
    tranaslations = TranslatedFields(
        name = models.CharField(
            max_length=settings.MAX_LENGTH, null=True, blank=True
        ),
        description = models.TextField(null=True, blank=True)
    )

    class Meta:
        abstract = True

    def __str__(self):
        # return "Name" from translation
        name = self.safe_translation_getter('name', str(self.pk))
        display_name = '%(id_code)s: %(name)s' % \
                {'name': name, 'id_code': self.id_code}
        return display_name


class VersionableArtefact(NameableArtefact):
    version = models.CharField(
        max_length=settings.MAX_LENGTH, \
        validators=[re_validators['VersionType']], default='1.0'
    )
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class MaintainableArtefact(VersionableArtefact):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
    )
    agencyID = models.CharField(max_length=settings.MAX_LENGTH)
    isFinal = models.BooleanField(default=False)
    #isExternalReference= models.BooleanField(default=False)
    tranaslations = TranslatedFields(
        name=models.CharField(max_length=settings.MAX_LENGTH),
    )

    class Meta:
        unique_together = ('id_code', 'agencyID', 'version')
        abstract = True


class ItemScheme(MaintainableArtefact):
    #isPartial = models.BooleanField(default=False)

    class Meta(MaintainableArtefact.Meta):
        abstract = True


class Item(NameableArtefact):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        unique=True,
    )
    tranaslations = TranslatedFields(
        name = models.CharField(max_length=settings.MAX_LENGTH),
    )

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
    textType = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True, choices=data_types)
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
    dimension_type = models.CharField(max_length=settings.MAX_LENGTH, choices = dimension_types, null=True, blank=True)
    objectType = models.CharField(max_length=settings.MAX_LENGTH, choices = object_types, null=True, blank=True)
    ConceptIdentity = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    LocalRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    ConceptRole= models.ManyToManyField(Reference, related_name='+')
    GroupDimensions = models.ManyToManyField(Reference, related_name='+')
    AttachmentConstraint = models.ManyToManyField(Reference, related_name='+')
    translations = TranslatedFields()
