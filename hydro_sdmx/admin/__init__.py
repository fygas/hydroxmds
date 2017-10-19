from django.contrib import admin

#Importing model objects
from ..models.organisation import OrganisationScheme, Organisation 
from ..models.codelist import Code, Codelist 
from ..models.conceptscheme import Concept, ConceptScheme
from ..models.data_structly import DataStructure, Dataflow, Group
from ..models.provision import DataProvisionAgreement
from ..models.constraint import AttachmentConstraint, ContentConstraint

#Importing admin objects
from .organisation import OrganisationSchemeAdmin, OrganisationAdmin
from .codelist import CodelistAdmin, CodeAdmin 
from .conceptscheme import ConceptAdmin, ConceptSchemeAdmin
from .data_structly import DataStructureAdmin, DataflowAdmin
from .provision import DataProvisionAgreementAdmin
from .constraint import AttachmentConstraintAdmin, ContentConstraintAdmin

admin.site.register(OrganisationScheme, OrganisationSchemeAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Codelist, CodelistAdmin)
admin.site.register(ConceptScheme, ConceptSchemeAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(Group, admin.ModelAdmin)
admin.site.register(DataStructure, DataStructureAdmin)
admin.site.register(Dataflow, DataflowAdmin)
admin.site.register(DataProvisionAgreement, DataProvisionAgreementAdmin)
admin.site.register(AttachmentConstraint, AttachmentConstraintAdmin)
admin.site.register(ContentConstraint, ContentConstraintAdmin)

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
