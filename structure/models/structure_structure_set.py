from django.db import models
from .structure_base import MaintainableArtefact, NameableArtefact 
from common.models import Reference
from hvad.models import TranslatedFields

# Abstract models
class ItemSchemeMap(MaintainableArtefact):
    class Meta:
        abstract = True
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)

class ItemAssociation(ItemSchemeMap):
    class Meta:
        abstract = True

# Concrete models
class StructureSet(MaintainableArtefact):
    RelatedStructures = models.ManyToManyField(Reference, on_delete=models.CASCADE, null=True, blank=True)
    OrganisationSchemeMaps = models.ManyToManyField('OrganisationSchemeMap', on_delete=models.CASCADE, null=True, blank=True)
    CategorySchemeMaps = models.ManyToManyField('CategorySchemeMap', on_delete=models.CASCADE, null=True, blank=True)
    CodelistMaps = models.ManyToManyField('CodelistMap', on_delete=models.CASCADE, null=True, blank=True)
    ConceptSchemeMaps = models.ManyToManyField('ConceptSchemeMap', on_delete=models.CASCADE, null=True, blank=True)
    ReportingTaxonomyMaps = models.ManyToManyField('ReportingTaxonomyMap', on_delete=models.CASCADE, null=True, blank=True)
    HybridCodelistMaps = models.ManyToManyField('HybridCodelistMap', on_delete=models.CASCADE, null=True, blank=True)
    StructureMaps = models.ManyToManyField('StructureMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class OrganisationSchemeMap(ItemSchemeMap):
    OrganisationMaps = models.ManyToManyField('OrganisationMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class OrganisationMap(ItemAssociation):
    translations = TranslatedFields()

class CategorySchemeMap(ItemSchemeMap):
    CategoryMaps = models.ManyToManyField('CategoryMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class CategoryMap(ItemAssociation):
    translations = TranslatedFields()

class CodelistMap(ItemSchemeMap):
    CodeMaps = models.ManyToManyField('CodeMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class CodeMap(ItemAssociation):
    translations = TranslatedFields()

class ConceptSchemeMap(ItemSchemeMap):
    ConceptMaps = models.ManyToManyField('ConceptMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class ConceptMap(ItemAssociation):
    translations = TranslatedFields()

class ReportingTaxonomyMap(ItemSchemeMap):
    ReportingCategoryMaps = models.ManyToManyField('ReportingCategoryMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class ReportingCategoryMap(ItemAssociation):
    translations = TranslatedFields()

class HybridCodelistMap(NameableArtefact):
    Source = models.ForeignKey('Reference', on_delete=models.CASCADE, null=True, blank=True)
    Target = models.ForeignKey('Reference', on_delete=models.CASCADE, null=True, blank=True)
    HybridCodeMaps = models.ManyToManyField('HybridCodeMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class HybridCodeMap(ItemAssociation):
    translations = TranslatedFields()

class StructureMap(NameableArtefact):
    Source = models.ForeignKey('Reference', on_delete=models.CASCADE, null=True, blank=True)
    Target = models.ForeignKey('Reference', on_delete=models.CASCADE, null=True, blank=True)
    ComponentMaps = models.ManyToManyField('ComponentMap', on_delete=models.CASCADE, null=True, blank=True)
    isExtension = models.BooleanField(null=True, blank=True, default=False)
    translations = TranslatedFields()

class ComponentMap(ItemAssociation):
    RepresentationMapping = models.ForeignKey('RepresentationMap', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class RepresentationMap(models.Model):
    CodelistMap = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
