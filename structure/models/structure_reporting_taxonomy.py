from django.db import models
from hvad.models import TranslatedFields
from .structure_base import ItemScheme, Item
from common.models import Reference

#ReportingTaxonomy Structure
class ReportingTaxonomy(ItemScheme):
    ReportingCategories = models.ManyToManyField('ReportingCategory', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class ReportingCategory(Item):
    ReportingCategories = models.ManyToManyField('self', on_delete=models.CASCADE, null=True, blank=True)
    StructuralMetadata = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    ProvisioningMetadata = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
