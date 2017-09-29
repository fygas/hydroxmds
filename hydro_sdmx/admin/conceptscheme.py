
from .base import MaintainableArtefactAdmin, ItemAdmin, ItemStackedInline

from ..models.conceptscheme import Concept

class ConceptAdmin(ItemAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[1][1]['fields'] = (
            'representation',
            'parent',
            'iso_concept_reference',
            ('description', 'uri'), 
            'annotations'
        ) 
        return fieldsets 

class ConceptStackedInline(ItemStackedInline):
    model = Concept
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[1][1]['fields'] = (
            'representation',
            'parent',
            'iso_concept_reference',
            ('description', 'uri'), 
            'annotations'
        ) 
        return fieldsets 

class ConceptSchemeAdmin(MaintainableArtefactAdmin):
    inlines = [ConceptStackedInline]

