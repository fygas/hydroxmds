from django.db import models
from hvad.models import TranslatedFields

from ..models import Item, ItemScheme

class CategoryScheme(ItemScheme):
    categories = models.ManyToManyField('Category', related_name='+')
    translations = TranslatedFields()

class Category(Item):
    #check this
    Categories = models.ManyToManyField('self')
    translations = TranslatedFields()

