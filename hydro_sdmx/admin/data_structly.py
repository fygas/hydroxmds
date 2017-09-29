from ..models.data_structly import Dimension, Attribute
from .base import ItemBaseStackedInline, MaintainableArtefactAdmin

class DimensionInline(ItemBaseStackedInline):
    model = Dimension
    filter_horizontal = ('annotations', 'roles', 'groups')
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'concept'),
                ('dimension_type', 'representation', 'measure_representation'),
                'position'
            ),
        }),
        ('Additional information', {
            'fields': (
                ('is_concept_role', 'roles'),
                'groups'
            ),
            'classes': ('collapse',)
        }),
        ('Annotations', {
            'fields': ('annotations',),
            'classes': ('collapse',),
        }),
    ] 

class AttributeInline(ItemBaseStackedInline):
    model = Attribute 
    filter_horizontal = ('annotations', 'attached2dims', 'attached2groups')
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'concept'),
                ('representation', 'required'),
            ),
        }),
        ('Additional information', {
            'fields': (
                ('is_concept_role', 'roles'),
                'groups'
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
        ('Annotations', {
            'fields': ('annotations',),
            'classes': ('collapse',),
        }),
    ] 

class DataStructureAdmin(MaintainableArtefactAdmin):
    filter_horizontal = ('annotations', 'dimension_annotations', 'measure_annotations', 'attribute_annotations')
    fieldsets = [ 
        (None, {
            'fields': ('id_code', 'name', 'version'),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': (
                ('description', 'uri'),
                'annotations'
            )
        }),
    ] 

# from .base import IdentifiableArtefactAdmin
# from django.contrib import admin
# from ..models.data_structly import Dimension, Attribute
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
