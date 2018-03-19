from nested_admin import NestedStackedInline
from ..models.data_structly import Dimension, Attribute, Group 
from .annotation import AnnotationNestedStackedInline
from .base import MaintainableArtefactAdmin 
from .base_nested_inline import RepresentedItemNestedStackedInline
from .common import NameNestedTabularInline, DescriptionNestedTabularInline

class DimensionNestedStackedInline(RepresentedItemNestedStackedInline):
    inlines = [AnnotationNestedStackedInline]
    model = Dimension
    filter_horizontal = ('roles',)
    fieldsets = [ 
        (None, {
            'fields': (
                ('dimension_type', 'id_code'),
                ('concept', 'position'),
            )
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('Optional Representation', {
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
        ('Measure Representation', {
            'fields': (
                ('measure_representation',),
            ),
            'classes': ('collapse',)
        }),
        ('Additional information', {
            'fields': (
                ('is_concept_role', 'uri'),
                'roles',
            ),
            'classes': ('collapse',)
        }),
    ] 
    inlines = (AnnotationNestedStackedInline,)

class AttributeNestedStackedInline(RepresentedItemNestedStackedInline):
    inlines = [AnnotationNestedStackedInline]
    model = Attribute 
    filter_horizontal = ('roles', 'attached2dimensions')
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'concept', 'required'),
            ),
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('Optional Representation', {
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
        ('Additional information', {
            'fields': (
                ('is_concept_role', 'roles'),
            ),
            'classes': ('collapse',)
        }),
        ('Attachments', {
            'fields': (
                'attached2dataset',
                'attached2group',
                'attached2dimensions',
                'attached2measure'
            ),
            'classes': ('collapse',)
        }),
    ] 

class GroupNestedStackedInline(NestedStackedInline):
    model = Group
    inlines = (AnnotationNestedStackedInline,)
    classes = ('collapse',)
    fieldsets = [ 
        (None, {
            'fields': (
                'group_id', 
                'dimensions',
                'attachment_constraint'
            )
        }),
    ]

class DataStructureAdmin(MaintainableArtefactAdmin):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, DimensionNestedStackedInline, GroupNestedStackedInline, AttributeNestedStackedInline, AnnotationNestedStackedInline]
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'agency', 'version'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Duration', {
            'fields': (
                ('valid_from', 'valid_to'), 
            ),
            'classes': ('collapse',)
        }),
        ('Observation', {
            'fields': (
                'obs_concept',
                ('enumeration', 'text_type',),
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
    list_filter = ['version', 'agency']

class DataflowAdmin(MaintainableArtefactAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'agency', 'version'),
                'structure',
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Duration', {
            'fields': (
                ('valid_from', 'valid_to'), 
            ),
            'classes': ('collapse',)
        }),
    ] 
