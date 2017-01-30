from django.db import models
from .structure_base import Item, ItemScheme
from hvad.models import TranslatedFields

class CategoryScheme(ItemScheme):
    categories = models.ManyToManyField('Category', null=True, blank=True)
    translations = TranslatedFields()

class Category(Item):
    #check this
    Categories = models.ManyToManyField('self', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
