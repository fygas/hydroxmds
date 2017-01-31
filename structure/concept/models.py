from django.db import models
from hvad.models import TranslatedFields

from common.models import ISOConceptReference
from ..models import Item, ItemScheme, Representation 

class ConceptScheme(ItemScheme):
    Concepts = models.ManyToManyField('Concept', related_name='+')
    translations = TranslatedFields()

class Concept(Item):
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    CoreRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    ISOConceptReference = models.ForeignKey(ISOConceptReference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    translations = TranslatedFields()

