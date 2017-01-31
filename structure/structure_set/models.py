from django.db import models
from hvad.models import TranslatedFields

from ..models import MaintainableArtefact, NameableArtefact 
from common.models import Reference

# Abstract models
class ItemSchemeMap(MaintainableArtefact):
    class Meta:
        abstract = True
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')

class ItemAssociation(ItemSchemeMap):
    class Meta:
        abstract = True

# Concrete models
class StructureSet(MaintainableArtefact):
    RelatedStructures = models.ManyToManyField(Reference, related_name='+')
    OrganisationSchemeMaps = models.ManyToManyField('OrganisationSchemeMap', related_name='+')
    CategorySchemeMaps = models.ManyToManyField('CategorySchemeMap', related_name='+')
    CodelistMaps = models.ManyToManyField('CodelistMap', related_name='+')
    ConceptSchemeMaps = models.ManyToManyField('ConceptSchemeMap', related_name='+')
    ReportingTaxonomyMaps = models.ManyToManyField('ReportingTaxonomyMap', related_name='+')
    HybridCodelistMaps = models.ManyToManyField('HybridCodelistMap', related_name='+')
    StructureMaps = models.ManyToManyField('StructureMap', related_name='+')
    translations = TranslatedFields()

class OrganisationSchemeMap(ItemSchemeMap):
    OrganisationMaps = models.ManyToManyField('OrganisationMap', related_name='+')
    translations = TranslatedFields()

class OrganisationMap(ItemAssociation):
    translations = TranslatedFields()

class CategorySchemeMap(ItemSchemeMap):
    CategoryMaps = models.ManyToManyField('CategoryMap', related_name='+')
    translations = TranslatedFields()

class CategoryMap(ItemAssociation):
    translations = TranslatedFields()

class CodelistMap(ItemSchemeMap):
    CodeMaps = models.ManyToManyField('CodeMap', related_name='+')
    translations = TranslatedFields()

class CodeMap(ItemAssociation):
    translations = TranslatedFields()

class ConceptSchemeMap(ItemSchemeMap):
    ConceptMaps = models.ManyToManyField('ConceptMap', related_name='+')
    translations = TranslatedFields()

class ConceptMap(ItemAssociation):
    translations = TranslatedFields()

class ReportingTaxonomyMap(ItemSchemeMap):
    ReportingCategoryMaps = models.ManyToManyField('ReportingCategoryMap', related_name='+')
    translations = TranslatedFields()

class ReportingCategoryMap(ItemAssociation):
    translations = TranslatedFields()

class HybridCodelistMap(NameableArtefact):
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    HybridCodeMaps = models.ManyToManyField('HybridCodeMap', related_name='+')
    translations = TranslatedFields()

class HybridCodeMap(ItemAssociation):
    translations = TranslatedFields()

class StructureMap(NameableArtefact):
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    ComponentMaps = models.ManyToManyField('ComponentMap', related_name='+')
    isExtension = models.NullBooleanField(null=True, blank=True)
    translations = TranslatedFields()

class ComponentMap(ItemAssociation):
    RepresentationMapping = models.ForeignKey('RepresentationMap', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    translations = TranslatedFields()

class RepresentationMap(models.Model):
    CodelistMap = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    translations = TranslatedFields()
