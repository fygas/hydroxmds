from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from .common import NameNestedTabularInline, DescriptionNestedTabularInline

from ..models.constraint import KeyValue, Key, ConstraintKeySet, CodeValueDetail, KeyValueSet, CubeRegion
from .annotation import AnnotationNestedStackedInline
from .base import MaintainableArtefactAdmin

class KeyValueNestedTabularInline(NestedTabularInline):
    model = KeyValue
    raw_id_fields = ('dimensions',)
    classes = ['collapse']
    fields = ('component_id', 'code_value', 'string_value')

class KeyNestedTabularInline(NestedTabularInline):
    model = Key 
    classes = ['collapse']
    inlines = [KeyValueNestedTabularInline]

class AttachmentConstraintKeySetNestedTabularInline(NestedTabularInline):
    model = ConstraintKeySet
    classes = ['collapse']
    inlines = [KeyNestedTabularInline]
    exclude = ('content_constraint',)

class AttachmentConstraintAdmin(MaintainableArtefactAdmin):
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
        ('Attachments', {
            'fields': (
                'datasources',
                'provisions',
                'dataflows',
                'data_structures',
                'datasets', 
            ),
            'classes': ('collapse',),
        }),
    ] 
    list_filter = ['version', 'agency', 'dataflows', 'data_structures']
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline, AttachmentConstraintKeySetNestedTabularInline]

class CodeValueDetailNestedTabularInline(NestedTabularInline):
    model = CodeValueDetail
    fields = ('code', 'cascade')
    classes = ('collapse',)

class KeyValueSetNestedStackedInline(NestedStackedInline):
    model = KeyValueSet
    inlines = [CodeValueDetailNestedTabularInline,]
    fieldsets = [ 
        (None, {
            'fields': ('component_id',),
        }),
        ('time_value', {
            'fields': (
                ('start_time', 'end_time',),
                ('start_inclusive', 'end_inclusive',)
            ),
            'classes': ('collapse',),
        }),
        ('string_values', {
            'fields': ('string_values',),
            'classes': ('collapse',),
        }),
    ]

class CubeRegionNestedTabularInline(NestedTabularInline):
    model = CubeRegion 
    fields = ('is_included',)
    inlines = [KeyValueSetNestedStackedInline]

class ContentConstraintKeySetNestedTabularInline(NestedTabularInline):
    model = ConstraintKeySet
    classes = ['collapse']
    inlines = [KeyNestedTabularInline]
    exclude = ('attachment_constraint',)

class ContentConstraintAdmin(MaintainableArtefactAdmin, NestedModelAdmin):
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
        ('Attachments', {
            'fields': (
                'datasource',
                'provisions',
                'dataflows',
                'data_structures',
                'dataset', 
            ),
            'classes': ('collapse',),
        }),
        ('Data provider attachments', {
            'fields': (
                'dataprovider',
                ('periodicity', 'offset', 'tolerance'),
                ('start_time', 'end_time'),
            ),
            'classes': ('collapse',),
        }),
    ] 
    list_filter = ['version', 'agency', 'dataflows', 'data_structures']
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline, ContentConstraintKeySetNestedTabularInline, CubeRegionNestedTabularInline]

class KeyValueTabularInline(admin.TabularInline):
    model = KeyValue
    classes = ['collapse']
    fields = ('component_id', 'code_value', 'string_value')

class KeyAdmin(admin.ModelAdmin):
    inlines = [KeyValueTabularInline]

# from django.contrib import admin
#
# from .base import MaintainableArtefactAdmin
#
# class AttachmentConstraintManager(MaintainableArtefactAdmin):
#     list_filter = (
#         ('agency', admin.RelatedOnlyFieldListFilter),
#         'version', 
#         ('attached2provisions', admin.RelatedOnlyFieldListFilter),
#         ('attached2dsds', admin.RelatedOnlyFieldListFilter),
#         ('attached2dataflows', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasets', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasources', admin.RelatedOnlyFieldListFilter)
#     )
#
# class ContentConstraintManager(MaintainableArtefactAdmin):
#     list_filter = (
#         ('agency', admin.RelatedOnlyFieldListFilter),
#         'version', 
#         ('attached2dataproviders', admin.RelatedOnlyFieldListFilter),
#         ('attached2provisions', admin.RelatedOnlyFieldListFilter),
#         ('attached2dsds', admin.RelatedOnlyFieldListFilter),
#         ('attached2dataflows', admin.RelatedOnlyFieldListFilter),
#         ('attached2dataset', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasource', admin.RelatedOnlyFieldListFilter)
#     )
#     
# class DataKeySetAdmin(admin.ModelAdmin):
#     list_filter = (
#         ('attachment_constraint', admin.RelatedOnlyFieldListFilter),
#         ('content_constraint', admin.RelatedOnlyFieldListFilter)
#     )
#
# class ConstraintDataKey(admin.ModelAdmin):
#     list_filter = ('data_key_set',)
#     list_display = ('data_key_set', 'data_key')
#
# class KeyValue(admin.ModelAdmin):
#     list_filter = ('constraint_data_key__data_key_set',)
#
# class CubeRegionManager(admin.ModelAdmin):
#     list_filter = (
#         ('content_constraint', admin.RelatedOnlyFieldListFilter)
#     )
#     list_display = ('content_constraint__id_code', 'region')
#
# class KeyValueSet(admin.ModelAdmin):
#     list_filter = ('cube_region',)
#
# class MetaattachmentConstraintManager(MaintainableArtefactAdmin):
#     list_filter = (
#         ('agency', admin.RelatedOnlyFieldListFilter),
#         'version', 
#         ('attached2metaprovisions', admin.RelatedOnlyFieldListFilter),
#         ('attached2metadsds', admin.RelatedOnlyFieldListFilter),
#         ('attached2metadataflows', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasets', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasources', admin.RelatedOnlyFieldListFilter)
#     )
#
# class MetacontentConstraintManager(MaintainableArtefactAdmin):
#     list_filter = (
#         ('agency', admin.RelatedOnlyFieldListFilter),
#         'version', 
#         ('attached2dataproviders', admin.RelatedOnlyFieldListFilter),
#         ('attached2metaprovisions', admin.RelatedOnlyFieldListFilter),
#         ('attached2metadsds', admin.RelatedOnlyFieldListFilter),
#         ('attached2metadataflows', admin.RelatedOnlyFieldListFilter),
#         ('attached2dataset', admin.RelatedOnlyFieldListFilter),
#         ('attached2datasource', admin.RelatedOnlyFieldListFilter)
#     )
#
# class MetadataKeySetAdmin(admin.ModelAdmin):
#     list_filter = (
#         ('metaattachment_constraint', admin.RelatedOnlyFieldListFilter),
#         ('metacontent_constraint', admin.RelatedOnlyFieldListFilter)
#     )
