from .annotation import AnnotationNestedStackedInline
from .base import RepresentedItemWithParentAdmin, MaintainableArtefactAdmin
from .base_nested_inline import RepresentedItemWithParentNestedStackedInline 
from .common import NameNestedTabularInline, DescriptionNestedTabularInline

from ..models.conceptscheme import Concept

class ConceptAdmin(RepresentedItemWithParentAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('wrapper', 'id_code'),
                ('parent', 'iso_concept_reference'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('More Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multi_lingual'),
            'classes': ('collapse',)
        }),
    ]

class ConceptNestedStackedInline(RepresentedItemWithParentNestedStackedInline):
    model = Concept
    fieldsets = [ 
        ('Identification', {
            'fields': (
                'id_code',
                ('parent', 'iso_concept_reference'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('More Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multi_lingual'),
            'classes': ('collapse',)
        }),
    ]

class ConceptSchemeAdmin(MaintainableArtefactAdmin):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline, ConceptNestedStackedInline]
