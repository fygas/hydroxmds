from django.db import models
from hvad.models import TranslatedFields

from common.constants import max_length

from ..models import MaintainableArtefact, NameableArtefact, IdentifiableArtefact, TextFormatInfo
from common.models import Reference

#HierarchicalCodelist Structure
class HierarchicalCodelist(MaintainableArtefact):
    IncludedCodelists = models.ManyToManyField(Reference, related_name='+')
    Hierarchies = models.ManyToManyField('Hierarchy', related_name='+')
    translations = TranslatedFields()

class Hierarchy(NameableArtefact):
    HierarchicalCode = models.ManyToManyField('HierarchicalCode', related_name='+')
    Level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, blank=True)
    leveled = models.NullBooleanField(null=True, blank=True)
    translations = TranslatedFields()

class Level(NameableArtefact):
    CodingFormat = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Level = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class HierarchicalCode(IdentifiableArtefact):
    Code = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    CodelistAliasRef = models.CharField(max_length=max_length['id'], null=True, blank=True)
    CodeID = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    HierarchicalCodes = models.ManyToManyField('self')
    Level = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    version = models.CharField(max_length=max_length['id'], null=True, blank=True)
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo= models.DateTimeField(null=True, blank=True)
    translations = TranslatedFields()
