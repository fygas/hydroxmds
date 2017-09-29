from django.contrib import admin

#Importing model objects
from ..models.annotation import Annotation  
from ..models.organisation import Organisation, Contact
from ..models.organisation_scheme import AgencyScheme, DataProviderScheme, DataConsumerScheme, OrganisationUnitScheme
from ..models.codelist import Code, Codelist, Representation, TextFormatInfo
from ..models.conceptscheme import Concept, ConceptScheme

#Importing admin objects
from .annotation import AnnotationAdmin
from .base import NameableArtefactAdmin, ItemAdmin
from .organisation import ContactAdmin, OrganisationSchemeOrganisationsAdmin
from .codelist import CodelistAdmin, RepresentationAdmin, TextFormatInfoAdmin
from .conceptscheme import ConceptAdmin, ConceptSchemeAdmin

admin.site.register(Organisation, NameableArtefactAdmin)
admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Contact, ContactAdmin)
models = [AgencyScheme, DataConsumerScheme, DataProviderScheme, OrganisationUnitScheme] 
for model in models:
    admin.site.register(model, OrganisationSchemeOrganisationsAdmin)
admin.site.register(Codelist, CodelistAdmin)
admin.site.register(Code, ItemAdmin)
admin.site.register(Representation, RepresentationAdmin)
admin.site.register(TextFormatInfo, TextFormatInfoAdmin)
admin.site.register(ConceptScheme, ConceptSchemeAdmin)
admin.site.register(Concept, ConceptAdmin)

# from .base import (
#     NameableArtefactAdmin, MaintainableArtefactAdmin, ItemAdmin,
#     IdentifiableArtefactAdmin, StructureItemAdmin
# )
# from .annotation import AnnotationAdmin
# from .registration import RegistrationAdmin
# from .codelist import TextFormatInfoAdmin
# from .data_structly import AttributeAdmin, DimensionAdmin
#
# from ..models.annotation import Annotation
# from ..models.registration import Source, Dataset, Metadataset, MetaStructure
# from ..models.organisation import (
#     Organisation, Contact, TelFax, X400, URI, Email
# )
# from ..models.organisation_scheme import (
#     AgencyScheme, DataConsumerScheme, DataProviderScheme,
#     OrganisationUnitScheme
# )
# from ..models.codelist import (
#     Codelist, Code, TextFormatInfo, Representation
# )
# from ..models.conceptscheme import Concept, ConceptScheme
# from ..models.hierarchical_codelist import (
#     HierarchicalCodelist, Hierarchy, HierarchicalCode, Level
# ) 
# from ..models.data_structly import (
#     DataStructure, Dataflow, Group, Dimension, ObsValue, Attribute
# )
# from ..models.metadata_structly import (
#     MetadataStructure, Metadataflow, MetadataTarget, MetadataTargetComponent,
#     Report, MetadataAttribute
# )
# from ..models.provision import (
#     DataProvisionAgreement, MetadataProvisionAgreement
# )
# from ..models.reference import ReferenceObject
# from ..models.constraint import (
#     AttachmentConstraint, ContentConstraint, DataKeySet, ConstraintDataKey, KeyValue,
#     CubeRegion, KeyValueSet, CodeValueDetail, MetaConstraint,
#     MetaattachmentConstraint, MetacontentConstraint, MetadataKeySet,
#     MetadataKey, MetadataKeyValue, MetadataTargetRegion, MetakeyValueSet,
#     MetaattrValueSet, DataAnyKey, DataAnyKeyValue, TimeValue
# )
# from .categorization_info import (
#     CategoryScheme, Category, Categorization, ReportingTaxonomy,
#     ReportingCategory
# ) 
# from .process import (
#     Process, ProcessStep, Computation, Transition, Condition
# )
# from .structure_set import (
#     StructureSet,  OrganisationSchemeMap, OrganisationMap, CategorySchemeMap,
#     CategoryMap, CodelistMap, CodeMap, ConceptSchemeMap, ConceptMap,
#     ReportingTaxonomyMap, ReportingCategoryMap, HybridCodelistMap,
#     HybridCodeMap, DataStructureMap, DataflowStructureMap, DataComponentMap,
#     MetadataStructureMap, MetadataflowStructureMap, MetadataComponentMap,
#     RepresentationMap, ValueMapping  
# )
# from .data import (
#     DataPartialKey, DataPartialKeyValue, DataMeasureKey, DataKey, AttrValue,
#     Obs, MetadataDataTarget, MetadataDataTargetValue,
#     MetadataDataAttributeValue, MetadataDataAttribute,
#     MetadataDataAttributeOrderedValue, MetadataAttributeString,
#     DataDimensionString, TimeValue
# )

# # Register models.annotation.models
# admin.site.register(Annotation, AnnotationAdmin)
#
# # Register models.registration models
# admin.site.register(Source, admin.ModelAdmin)
# models = [Dataset, Metadataset, MetaStructure]
# for model in models:
#     admin.site.register(model, RegistrationAdmin)
#
# # Register models.organisation models
# admin.site.register(Organisation, NameableArtefactAdmin)
# models = [Contact, TelFax, X400, URI, Email]
# for model in models:
#     admin.site.register(model, admin.ModelAdmin)

# Register models.organisation_scheme models
# models = [AgencyScheme, DataConsumerScheme, DataProviderScheme, OrganisationUnitScheme]
# for model in models:
#     admin.site.register(model, MaintainableArtefactAdmin)
#
# # Register models.codelist models
# admin.site.register(Codelist, MaintainableArtefactAdmin)
# admin.site.register(Code, ItemAdmin)
# admin.site.register(TextFormatInfo, TextFormatInfoAdmin)
# admin.site.register(Representation, IdentifiableArtefactAdmin)
#
# # Register models.codelist models
# admin.site.register(ConceptScheme, MaintainableArtefactAdmin)
# admin.site.register(Concept, ItemAdmin)
#
# # Register models.hierarchical_codelist models
# admin.site.register(HierarchicalCodelist, MaintainableArtefactAdmin)
# admin.site.register(Hierarchy, NameableArtefactAdmin)
# admin.site.register(Level, NameableArtefactAdmin)
# admin.site.register(HierarchicalCode, IdentifiableArtefactAdmin)
#
# # Register models.data_structly models
# admin.site.register(DataStructure, MaintainableArtefactAdmin)
# admin.site.register(Dataflow, MaintainableArtefactAdmin)
# admin.site.register(Group, IdentifiableArtefactAdmin)
# admin.site.register(Dimension, DimensionAdmin)
# admin.site.register(Attribute, AttributeAdmin)
# admin.site.register(ObsValue, admin.ModelAdmin)
#
# # Register models.metadata_structly models
# admin.site.register(MetadataStructure, MaintainableArtefactAdmin)
# admin.site.register(Metadataflow, MaintainableArtefactAdmin)
# admin.site.register(MetadataTarget, IdentifiableArtefactAdmin)
# admin.site.register(MetadataTargetComponent, IdentifiableArtefactAdmin)
# admin.site.register(Report, MaintainableArtefactAdmin)
# admin.site.register(MetadataAttribute, StructureItemAdmin)
#
# # Register models.provision models
# admin.site.register(DataProvisionAgreement, MaintainableArtefactAdmin)
# admin.site.register(MetadataProvisionAgreement, MaintainableArtefactAdmin)
#
# # Register models.reference models
# admin.site.register(ReferenceObject, admin.ModelAdmin)
#
#
# # Register models.constraint models
# models = [AttachmentConstraint, ContentConstraint, MetaattachmentConstraint, MetacontentConstraint]
# for model in models:
#     admin.site.register(model, MaintainableArtefactAdmin)
#
#     DataKeySet, ConstraintDataKey, KeyValue,
#     CubeRegion, KeyValueSet, CodeValueDetail, MetaConstraint,
#     MetadataKeySet,
#     MetadataKey, MetadataKeyValue, MetadataTargetRegion, MetakeyValueSet,
#     MetaattrValueSet, DataAnyKey, DataAnyKeyValue, TimeValue
