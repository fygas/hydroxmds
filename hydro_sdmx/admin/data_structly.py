from nested_admin import TabularInline, NestedModelAdmin
from ..models.data_structly import Dimension, Attribute, Measure, Group
from .annotation import AnnotationNestedStackedInline
from .base import MaintainableArtefactAdmin 
from .base_nested_inline import RepresentedItemNestedStackedInline

class GroupNestedStackedInline(TabularInline):
    model = Group
    fields = ('id_code',)

class DimensionNestedStackedInline(RepresentedItemNestedStackedInline):
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
            )
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
                ('roles',),
            ),
            'classes': ('collapse',)
        }),
    ] 
    inlines = (GroupNestedStackedInline, AnnotationNestedStackedInline )

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
            )
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

class MeasureNestedStackedInline(RepresentedItemNestedStackedInline):
    model = Measure 
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'concept',),
            )
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            )
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
    ] 
    max_num = 1
    extra = 1

class DataStructureAdmin(MaintainableArtefactAdmin, NestedModelAdmin):
    inlines = [DimensionNestedStackedInline, MeasureNestedStackedInline, AttributeNestedStackedInline]

class DataflowAdmin(MaintainableArtefactAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] = (
            ('id_code', 'name'), 
            ('agency', 'version'),
            'structure',
        ) 
        return fieldsets 
