from .models import (
    Organisation
    # Annotation, Organisation, Contact, Telephone, Fax, X400, URI, Email
    # Annotation, Source, Dataset, Metadataset, MetaStructure, Organisation,
    # Contact, TelFax, X400, URI, Email, AgencyScheme, DataConsumerScheme,
    # DataProviderScheme, OrganisationUnitScheme, Codelist, Code, TextFormatInfo,
    # Representation, Concept, ConceptScheme,
    # HierarchicalCodelist, Hierarchy, HierarchicalCode, Level, DataStructure,
    # Dataflow, Group, Dimension, ObsValue, Attribute, MetadataStructure,
    # Metadataflow, MetadataTarget, MetadataTargetComponent, Report,
    # MetadataAttribute, DataProvisionAgreement, MetadataProvisionAgreement,
    # ReferenceObject, AttachmentConstraint, ContentConstraint, DataKeySet,
    # DataKey, KeyValue, CubeRegion, KeyValueSet, CodeValueDetail,
    # MetaConstraint, MetaattachmentConstraint, MetacontentConstraint,
    # MetadataKeySet, MetadataKey, MetadataKeyValue, MetadataTargetRegion,
    # MetakeyValueSet, MetaattrValueSet, DataAnyKey, DataAnyKeyValue, TimeValue,
    # CategoryScheme, Category, Categorization, ReportingTaxonomy,
    # ReportingCategory, Process, ProcessStep, Computation, Transition,
    # Condition, StructureSet,  OrganisationSchemeMap, OrganisationMap,
    # CategorySchemeMap, CategoryMap, CodelistMap, CodeMap, ConceptSchemeMap,
    # ConceptMap, ReportingTaxonomyMap, ReportingCategoryMap, HybridCodelistMap,
    # HybridCodeMap, DataStructureMap, DataflowStructureMap, DataComponentMap,
    # MetadataStructureMap, MetadataflowStructureMap, MetadataComponentMap,
    # RepresentationMap, ValueMapping  
) 
# from .forms import RegistrationForm 

from django.contrib import admin

# class RegistrationAdmin(admin.ModelAdmin):
#     list_filter = ('created_by', 'action', 'interactive')
#     search_fields = ('created_by', 'action', 'interactive')
#     list_display = ('created_by', 'actions', 'interactive')
#     form = RegistrationForm

# class AnnotationAdmin(admin.ModelAdmin):
#     list_filter = ('annotation_type',)
#     search_fields = ('annotation_type', 'id_code', 'annotation_title')
#     list_display = ('id_code', 'annotation_title', 'annotation_title')

# class TextFormatInfoAdmin(admin.ModelAdmin):
#     filter_horizontal = ('annotations', )
#     search_fields = ['id_code', 'name', 'text_type']
#     list_display = ('id_code', 'name', 'text_type',)
#     list_filter = ('text_type',)

class AnnotableArtefactAdmin(admin.ModelAdmin):
    filter_horizontal = ('annotations',)
    list_display = ('id',)

class IdentifiableArtefactAdmin(AnnotableArtefactAdmin):
    search_fields = ['id_code']
    list_display = ('id_code',)
    list_display_links = ('id_code',)

# class StructureItemAdmin(IdentifiableArtefactAdmin):
#     filter_horizontal = ('annotations', )
#     search_fields = ['wrapper', 'id_code', 'concept']
#     list_display = ('id_code', 'concept')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)
#
# class DimensionAdmin(IdentifiableArtefactAdmin):
#     filter_horizontal = ('annotations', 'roles', 'groups')
#     search_fields = ['wrapper', 'id_code', 'concept']
#     list_display = ('id_code', 'concept')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)
#
# class AttributeAdmin(IdentifiableArtefactAdmin):
#     filter_horizontal = ('annotations', 'roles', 'attached2dims', 'attached2groups')
#     search_fields = ['wrapper', 'id_code', 'concept']
#     list_display = ('id_code', 'concept')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)

class NameableArtefactAdmin(IdentifiableArtefactAdmin):
    search_fields = ['id_code', 'name']
    list_display = ('id_code', 'name')
    list_display_links = ('id_code', 'name')

# class ItemAdmin(NameableArtefactAdmin):
#     search_fields = ['wrapper', 'id_code', 'name']
#     list_display = ('id_code', 'name')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)
#
# class ItemSchemeMapAdmin(NameableArtefactAdmin):
#     search_fields = ['id_code', 'name', 'source', 'target' ]
#     list_display = ('id_code', 'name', 'source', 'target')
#     list_display_links = ('id_code',)
#     list_filter = ('source', 'target')
#
# class ItemMapAdmin(admin.ModelAdmin):
#     search_fields = ['wrapper', 'source', 'target']
#     list_display = ('wrapper', 'source', 'target')
#     list_filter = ('wrapper', 'source', 'target')
#     list_display_links = ('wrapper', 'source', 'target')
#
# class VersionableArtefactAdmin(NameableArtefactAdmin):
#     search_fields = ['id_code', 'name', 'version']
#     list_display = ('id_code', 'name', 'version')
#     list_display_links = ('id_code',)
#     list_filter = ('version',)
#
# class MaintainableArtefactAdmin(IdentifiableArtefactAdmin):
#     search_fields = ['id_code', 'name', 'version', 'agency']
#     list_display = ('id_code', 'name', 'version', 'agency')
#     list_display_links = ('id_code',)
#     list_filter = ('agency', 'version',)
#     form = RegistrationForm

model2admin = {}
#model2admin[AnnotationAdmin] = [Annotation]
# model2admin[TextFormatInfoAdmin] = [TextFormatInfo]
# model2admin[RegistrationAdmin] = [
#     Dataset, Metadataset, MetaStructure
# ]
# model2admin[IdentifiableArtefactAdmin] = [
#     Representation, HierarchicalCode, Group, MetadataTarget,
#     MetadataTargetComponent, Transition 
# ]
# model2admin[StructureItemAdmin] = [
#     MetadataAttribute
# ]
# model2admin[DimensionAdmin] = [
#     Dimension
# ]
# model2admin[AttributeAdmin] = [
#     Attribute 
# ]
model2admin[NameableArtefactAdmin] = [
    Organisation, 
    # Hierarchy, Level, ProcessStep,
]
# model2admin[ItemAdmin] = [
#     Code, Concept
# ]
# model2admin[MaintainableArtefactAdmin] = [
#     AgencyScheme, DataConsumerScheme, DataProviderScheme,
#     OrganisationUnitScheme, Codelist, ConceptScheme, HierarchicalCodelist,
#     DataStructure, Dataflow, MetadataStructure, Metadataflow, Report,
#     DataProvisionAgreement, MetadataProvisionAgreement, Process, StructureSet, AttachmentConstraint, ContentConstraint,
# ]
# model2admin[ItemSchemeMapAdmin] = [
#     OrganisationSchemeMap, CategorySchemeMap, CodelistMap, ConceptSchemeMap,
#     ReportingTaxonomyMap
# ]
#
# model2admin[ItemMapAdmin] = [
#     OrganisationMap, CategoryMap, CodeMap, ConceptMap, ReportingCategoryMap,
# ]
#
# model2admin[admin.ModelAdmin] = [
#     Source, Contact, TelFax, X400, URI, Email, ObsValue, ReferenceObject,
#     Computation, Condition, ValueMapping,
#     ##Improve
#     HybridCodelistMap, HybridCodeMap, DataComponentMap, MetadataComponentMap,
#     RepresentationMap, DataStructureMap, DataflowStructureMap,
#     MetadataStructureMap, MetadataflowStructureMap
# ]


for key, value in model2admin.items():
    for model in value:
        admin.site.register(model, key)
