from nested_admin import NestedModelAdmin
from ..models.data_structly import Dimension, Attribute, Group 
from .annotation import AnnotationNestedStackedInline
from .base import MaintainableArtefactAdmin 
from .base_nested_inline import RepresentedItemNestedStackedInline

class DimensionNestedStackedInline(RepresentedItemNestedStackedInline):
    model = Dimension
    filter_horizontal = ('groups', 'roles',)
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
                'is_multiLingual'),
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
                'groups',
            ),
            'classes': ('collapse',)
        }),
    ] 
    inlines = (AnnotationNestedStackedInline,)

class AttributeNestedStackedInline(RepresentedItemNestedStackedInline):
    model = Attribute 
    filter_horizontal = ('roles', 'attached2dims', 'attached2groups')
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
                'is_multiLingual'),
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
                'attached2dims',
                'attached2measure',
                'attached2dim_in_group',
                'attached2groups'
            ),
            'classes': ('collapse',)
        }),
    ] 

class GroupNestedStackedInline(NestedModelAdmin):
    model = Group
    inlines = (AnnotationNestedStackedInline,)
    classes = ('wrapper')
    fieldsets = [ 
        (None, {
            'fields': (
                'group_id', 
                'dimensions',
                'attachment_constraint'
            )
        }),
    ]

class DataStructureAdmin(MaintainableArtefactAdmin, NestedModelAdmin):
    inlines = [DimensionNestedStackedInline, GroupNestedStackedInline, AttributeNestedStackedInline, AnnotationNestedStackedInline]
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'name',),
                ('agency', 'version',),
            )
        }),
        ('Additional information', {
            'fields': (
                ('valid_from', 'valid_to'), 
                ('description', 'uri',),
            ),
            'classes': ('collapse',),
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
                'is_multiLingual'),
            'classes': ('collapse',)
        }),
    ] 
    list_filter = ['version', 'agency']

class DataflowAdmin(MaintainableArtefactAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] = (
            ('id_code', 'name'), 
            ('agency', 'version'),
            'structure',
        ) 
        return fieldsets 
