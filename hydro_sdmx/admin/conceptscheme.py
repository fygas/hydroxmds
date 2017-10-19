from nested_admin import NestedModelAdmin
from .annotation import AnnotationNestedStackedInline
from .base import RepresentedItemWithParentAdmin, MaintainableArtefactAdmin
from .base_nested_inline import RepresentedItemWithParentNestedStackedInline 

from ..models.conceptscheme import Concept

class ConceptAdmin(RepresentedItemWithParentAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[-1][1]['fields'] = (
            ('parent','iso_concept_reference'),
            ('description', 'uri'), 
        ) 
        return fieldsets 

class ConceptNestedStackedInline(RepresentedItemWithParentNestedStackedInline):
    model = Concept
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[-1][1]['fields'] = (
            ('parent','iso_concept_reference'),
            ('description', 'uri'), 
        ) 
        return fieldsets 

class ConceptSchemeAdmin(NestedModelAdmin, MaintainableArtefactAdmin):
    inlines = [ConceptNestedStackedInline, AnnotationNestedStackedInline]
