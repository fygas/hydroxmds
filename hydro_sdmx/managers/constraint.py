from django.db import models

class AttachmentConstraintManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.prefetch_related('datasets', 'datasources', 'provisions', 'data_structures', 'dataflows')

class ContentConstraintManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('dataset', 'datasource').prefetch_related('dataproviders', 'provisions', 'data_structures', 'dataflows')

class DataKeySetManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('attachment_constraint', 'content_constraint')

class ConstraintDataKeyManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('constraint_key_set').prefetch_related('key_values')

class KeyValueManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('code_value')

class CubeRegionManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('constraint').prefetch_related('key_value_sets')

class KeyValueSetManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        qs = super_qs.select_related('data_key', 'dimension', 'attribute')
        return qs.prefetch_related('code_value_details', 'string_values')

class CodeValueDetailManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('code')

class MetaattachmentConstraintManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.prefetch_related('attached2datasets', 'attached2datasources', 'attached2metaprovisions', 'attached2metadsds', 'attached2metadataflows')

class MetacontentConstraintManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('attached2dataset', 'attached2datasource').prefetch_related('attached2dataproviders', 'attached2metaprovisions', 'attached2metadsds', 'attached2metadataflows')

class MetadataKeySetManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('metaattachment_constraint', 'metacontent_constraint')

class MetadataKeyValueManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return super_qs.select_related('metadata_key', 'target_component', 'value', 'dataset', 'data_key', 'objekt')
