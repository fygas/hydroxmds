from django.db import models
from .structure_base import MaintainableArtefact, NameableArtefact, IdentifiableArtefact
from common.models import Reference, TextFormat
from . import enum
from hvad.models import TranslatedFields

#HierarchicalCodelist Structure
class HierarchicalCodelist(MaintainableArtefact):
    IncludedCodelists = models.ManyToManyField(Reference, on_delet=models.CASCADE, null=True, blank=True)
    Hierarchies = models.ManyToManyField('Hierarchy', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class Hierarchy(NameableArtefact):
    HierarchicalCode = models.ManyToManyField('HierarchicalCode', on_delete=models.CASCADE, null=True, blank=True)
    Level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, blank=True)
    leveled = models.BooleanField(null=True, blank=True, default=False)
    translations = TranslatedFields()

class Level(NameableArtefact):
    CodingFormat = models.ForeignKey(TextFormat, on_delete=models.CASCADE, null=True, blank=True)
    Level = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class HierarchicalCode(IdentifiableArtefact):
    Code = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    CodelistAliasRef = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    CodeID = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    HierarchicalCodes = models.ManyToManyField('self', on_delete=models.CASCADE, null=True, blank=True)
    Level = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    version = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo= models.DateTimeField(null=True, blank=True)
    translations = TranslatedFields()
