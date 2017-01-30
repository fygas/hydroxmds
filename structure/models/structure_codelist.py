from django.db import models
from .structure_base import Item, ItemScheme 
from hvad.models import TranslatedFields


class Codelist(ItemScheme):
    Codes = models.ManyToManyField('Code', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class Code(Item):
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
