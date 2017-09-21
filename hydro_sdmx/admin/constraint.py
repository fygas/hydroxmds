
from django.contrib import admin

from .base import MaintainableArtefactAdmin

class AttachmentConstraintManager(MaintainableArtefactAdmin):
    list_filter = (
        ('agency', admin.RelatedOnlyFieldListFilter),
        'version', 
        ('attached2provisions', admin.RelatedOnlyFieldListFilter),
        ('attached2dsds', admin.RelatedOnlyFieldListFilter),
        ('attached2dataflows', admin.RelatedOnlyFieldListFilter),
        ('attached2datasets', admin.RelatedOnlyFieldListFilter),
        ('attached2datasources', admin.RelatedOnlyFieldListFilter)
    )

class ContentConstraintManager(MaintainableArtefactAdmin):
    list_filter = (
        ('agency', admin.RelatedOnlyFieldListFilter),
        'version', 
        ('attached2dataproviders', admin.RelatedOnlyFieldListFilter),
        ('attached2provisions', admin.RelatedOnlyFieldListFilter),
        ('attached2dsds', admin.RelatedOnlyFieldListFilter),
        ('attached2dataflows', admin.RelatedOnlyFieldListFilter),
        ('attached2dataset', admin.RelatedOnlyFieldListFilter),
        ('attached2datasource', admin.RelatedOnlyFieldListFilter)
    )
    
class DataKeySetAdmin(admin.ModelAdmin):
    list_filter = (
        ('attachment_constraint', admin.RelatedOnlyFieldListFilter),
        ('content_constraint', admin.RelatedOnlyFieldListFilter)
    )

class ConstraintDataKey(admin.ModelAdmin):
    list_filter = ('data_key_set',)
    list_display = ('data_key_set', 'data_key')

class KeyValue(admin.ModelAdmin):
    list_filter = ('constraint_data_key__data_key_set',)

class CubeRegionManager(admin.ModelAdmin):
    list_filter = (
        ('content_constraint', admin.RelatedOnlyFieldListFilter)
    )
    list_display = ('content_constraint__id_code', 'region')

class KeyValueSet(admin.ModelAdmin):
    list_filter = ('cube_region',)

class MetaattachmentConstraintManager(MaintainableArtefactAdmin):
    list_filter = (
        ('agency', admin.RelatedOnlyFieldListFilter),
        'version', 
        ('attached2metaprovisions', admin.RelatedOnlyFieldListFilter),
        ('attached2metadsds', admin.RelatedOnlyFieldListFilter),
        ('attached2metadataflows', admin.RelatedOnlyFieldListFilter),
        ('attached2datasets', admin.RelatedOnlyFieldListFilter),
        ('attached2datasources', admin.RelatedOnlyFieldListFilter)
    )

class MetacontentConstraintManager(MaintainableArtefactAdmin):
    list_filter = (
        ('agency', admin.RelatedOnlyFieldListFilter),
        'version', 
        ('attached2dataproviders', admin.RelatedOnlyFieldListFilter),
        ('attached2metaprovisions', admin.RelatedOnlyFieldListFilter),
        ('attached2metadsds', admin.RelatedOnlyFieldListFilter),
        ('attached2metadataflows', admin.RelatedOnlyFieldListFilter),
        ('attached2dataset', admin.RelatedOnlyFieldListFilter),
        ('attached2datasource', admin.RelatedOnlyFieldListFilter)
    )

class MetadataKeySetAdmin(admin.ModelAdmin):
    list_filter = (
        ('metaattachment_constraint', admin.RelatedOnlyFieldListFilter),
        ('metacontent_constraint', admin.RelatedOnlyFieldListFilter)
    )
