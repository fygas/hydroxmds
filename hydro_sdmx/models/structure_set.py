from django.db import models

from .abstract import NameableArtefact 
from .abstract_postorg import MaintainableArtefact
from .categorization_info import CategoryScheme, Category
from .categorization_info import ReportingTaxonomy, ReportingCategory
from .codelist import Codelist, Code, TextFormatInfo
from .common import Annotation
from .conceptscheme import Concept, ConceptScheme
from .data_structly import Dimension, ObsValue, Attribute, DataStructure, Dataflow
from .hierarchical_codelist import HierarchicalCodelist, HierarchicalCode
from .metadata_structly import MetadataTargetComponent, MetadataAttribute, MetadataStructure, Metadataflow
from .organisation import Organisation
from .reference import ReferenceObject

from ..constants import TOKENS
from ..settings import api_maxlen_settings
from ..validators import re_validators

class StructureSet(MaintainableArtefact):
    related_structures = models.ManyToManyField(ReferenceObject)
    organisation_scheme_maps = models.ManyToManyField('OrganisationSchemeMap')
    category_scheme_maps = models.ManyToManyField('CategorySchemeMap')
    codelist_maps = models.ManyToManyField('CodelistMap')
    concept_scheme_maps = models.ManyToManyField('ConceptSchemeMap')
    reporting_taxonomy_maps = models.ManyToManyField('ReportingTaxonomyMap')
    hybrid_codelist_maps = models.ManyToManyField('HybridCodelistMap')
    data_structure_maps = models.ManyToManyField('DataStructureMap')
    dataflow_structure_maps = models.ManyToManyField('DataflowStructureMap')
    metadata_structure_maps = models.ManyToManyField('MetadataStructureMap')
    metadataflow_structure_maps = models.ManyToManyField('MetadataflowStructureMap')

class ItemSchemeMap(NameableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
        unique=True
    )
    name = models.CharField(max_length=api_maxlen_settings.NAME)
    class Meta(NameableArtefact.Meta):
        abstract = True

class ItemMap(models.Model):
    annotations = models.ManyToManyField(Annotation)

    class Meta:
        abstract = True
        unique_together = ('wrapper', 'source', 'target')

class OrganisationSchemeMap(ItemSchemeMap):
    source = models.ForeignKey(ReferenceObject, on_delete=models.CASCADE, related_name='organisation_scheme_map_sources')
    target = models.ForeignKey(ReferenceObject, on_delete=models.CASCADE, related_name='organisation_scheme_map_targets')

class OrganisationMap(ItemMap):
    wrapper = models.ForeignKey(OrganisationSchemeMap, on_delete=models.CASCADE, related_name='organisation_maps')
    source = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='+')
    target = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='+')

class CategorySchemeMap(ItemSchemeMap):
    source = models.ForeignKey(CategoryScheme, on_delete=models.CASCADE, related_name='category_scheme_map_sources')
    target = models.ForeignKey(CategoryScheme, on_delete=models.CASCADE, related_name='category_scheme_map_targets')

class CategoryMap(ItemMap):
    wrapper = models.ForeignKey(CategorySchemeMap, on_delete=models.CASCADE, related_name='category_maps')
    source = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
    target = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')

class CodelistMap(ItemSchemeMap):
    source = models.ForeignKey(Codelist, on_delete=models.CASCADE, related_name='codelist_map_sources')
    target = models.ForeignKey(Codelist, on_delete=models.CASCADE, related_name='codelist_map_targets')

class CodeMap(ItemMap):
    wrapper = models.ForeignKey(CodelistMap, on_delete=models.CASCADE, related_name='code_maps')
    source = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='code_sources')
    target = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='code_targets')

class ConceptSchemeMap(ItemSchemeMap):
    source = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, related_name='concept_scheme_map_sources')
    target = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE, related_name='concept_scheme_map_targets')

class ConceptMap(ItemMap):
    wrapper = models.ForeignKey(ConceptSchemeMap, on_delete=models.CASCADE, related_name='concept_maps')
    source = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='+')
    target = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='+')

class ReportingTaxonomyMap(ItemSchemeMap):
    source = models.ForeignKey(ReportingTaxonomy, on_delete=models.CASCADE, related_name='reporting_taxonomy_map_sources')
    target = models.ForeignKey(ReportingTaxonomy, on_delete=models.CASCADE, related_name='reporting_taxonomy_map_targets')

class ReportingCategoryMap(ItemMap):
    wrapper = models.ForeignKey(ReportingTaxonomyMap, on_delete=models.CASCADE, related_name='reporting_category_maps')
    source = models.ForeignKey(ReportingCategory, on_delete=models.CASCADE, related_name='+')
    target = models.ForeignKey(ReportingCategory, on_delete=models.CASCADE, related_name='+')

class HybridCodelistMap(ItemSchemeMap):
    source_cl = models.ForeignKey(Codelist, null=True, blank=True, on_delete=models.CASCADE, related_name='hybrid_codelist_map_sources')
    source_hcl = models.ForeignKey(HierarchicalCodelist, null=True, blank=True, on_delete=models.CASCADE, related_name='hybrid_codelist_map_sources')
    target_cl = models.ForeignKey(Codelist, null=True, blank=True, on_delete=models.CASCADE, related_name='hybrid_codelist_map_targets')
    target_hcl = models.ForeignKey(HierarchicalCodelist, null=True, blank=True, on_delete=models.CASCADE, related_name='hybrid_codelist_map_targets')

class HybridCodeMap(ItemMap):
    wrapper = models.ForeignKey(HybridCodelistMap, on_delete=models.CASCADE, related_name='hybrid_code_maps')
    source_c = models.ForeignKey(Code, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    source_hc = models.ForeignKey(HierarchicalCode, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_c = models.ForeignKey(Code, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_hc = models.ForeignKey(HierarchicalCode, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    class Meta:
        unique_together = ('wrapper', 'source_c', 'source_hc', 'target_c', 'target_hc')

class DataStructureMap(ItemSchemeMap):
    source = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='data_structure_map_sources')
    target = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='data_structure_map_targets')
    is_extension = models.BooleanField(default=False)

class DataflowStructureMap(ItemSchemeMap):
    source = models.ForeignKey(Dataflow, on_delete=models.CASCADE, related_name='dataflow_structure_map_sources')
    target = models.ForeignKey(Dataflow, on_delete=models.CASCADE, related_name='dataflow_structure_map_targets')

class DataComponentMap(ItemMap):
    wrapper = models.ForeignKey(DataStructureMap, on_delete=models.CASCADE, related_name='data_component_maps')
    wrapper = models.ForeignKey(DataflowStructureMap, on_delete=models.CASCADE, related_name='data_component_maps')
    source_dim = models.ForeignKey(Dimension, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    source_obs = models.ForeignKey(ObsValue, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    source_attr = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    target_dim = models.ForeignKey(Dimension,  null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_obs = models.ForeignKey(ObsValue, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_attr = models.ForeignKey(Attribute, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    representation_mapping = models.ForeignKey('RepresentationMap', null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    class Meta:
        unique_together = ('wrapper', 'source_dim', 'source_obs', 'source_attr', 'target_dim', 'target_obs', 'target_attr', 'representation_mapping')

class MetadataStructureMap(ItemSchemeMap):
    source = models.ForeignKey(MetadataStructure, on_delete=models.CASCADE, related_name='metadata_structure_map_sources')
    target = models.ForeignKey(MetadataStructure, on_delete=models.CASCADE, related_name='metadata_structure_map_targets')
    is_extension = models.BooleanField(default=False)

class MetadataflowStructureMap(ItemSchemeMap):
    source = models.ForeignKey(Metadataflow, on_delete=models.CASCADE, related_name='metadataflow_structure_map_sources')
    target = models.ForeignKey(Metadataflow, on_delete=models.CASCADE, related_name='metadata_structure_map_targets')

class MetadataComponentMap(ItemMap):
    wrapper_structure = models.ForeignKey(MetadataStructureMap, on_delete=models.CASCADE, related_name='metadata_component_maps')
    wrapper_usage = models.ForeignKey(MetadataflowStructureMap, on_delete=models.CASCADE, related_name='metadata_component_maps')
    source_metacomp = models.ForeignKey(MetadataTargetComponent, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    source_metaattr = models.ForeignKey(MetadataAttribute, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_metacomp = models.ForeignKey(MetadataTargetComponent, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    target_metaattr = models.ForeignKey(MetadataAttribute, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    representation_mapping = models.ForeignKey('RepresentationMap', null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    class Meta:
        unique_together = ('wrapper_structure', 'wrapper_usage', 'source_metacomp', 'source_metaattr', 'target_metacomp', 'target_metaattr')

class RepresentationMap(models.Model):
    codelist_map = models.ForeignKey(CodelistMap, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    to_text_format = models.ForeignKey(TextFormatInfo, null=True, blank=True, on_delete=models.CASCADE, related_name='+') 
    to_value_type = models.CharField(max_length=api_maxlen_settings.TOKENS, choices=TOKENS)
    value_map = models.ManyToManyField('ValueMapping', related_name='+') 

class ValueMapping(models.Model):
    source = models.CharField(max_length=api_maxlen_settings.VALUE_MAP)
    target = models.CharField(max_length=api_maxlen_settings.VALUE_MAP)
