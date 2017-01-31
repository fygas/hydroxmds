from django.db import models
from hvad.models import TranslatedFields

from ..models import Item, ItemScheme 


class Codelist(ItemScheme):
    Codes = models.ManyToManyField('Code', related_name='+')
    translations = TranslatedFields()

class Code(Item):
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
