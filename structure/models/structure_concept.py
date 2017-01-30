from django.db import models
from .structure_base import Item, ItemScheme 
from .structure import ISOConceptReference, Representation
from hvad.models import TranslatedFields

class ConceptScheme(ItemScheme):
    Concepts = models.ManyToManyField('Concept', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class Concept(Item):
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    CoreRepresentation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True)
    ISOConceptReference = models.ForeignKey(ISOConceptReference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

