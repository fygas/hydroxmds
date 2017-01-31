from django.db import models
from hvad.models import TranslatedFields

from ..models import ItemScheme, Item
from common.models import Reference

#ReportingTaxonomy Structure
class ReportingTaxonomy(ItemScheme):
    ReportingCategories = models.ManyToManyField('ReportingCategory', related_name='+')
    translations = TranslatedFields()

class ReportingCategory(Item):
    ReportingCategories = models.ManyToManyField('self')
    StructuralMetadata = models.ManyToManyField(Reference, related_name='+')
    ProvisioningMetadata = models.ManyToManyField(Reference, related_name='+')
    translations = TranslatedFields()
