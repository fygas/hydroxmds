from .annotation import AnnotationNestedStackedInline
from django.contrib import admin
from nested_admin import NestedModelAdmin

class DatasetAttributeAdmin(admin.ModelAdmin):
    fields = (
        'dataset',
         'attribute',
        ('code_value', 'string_value')
    )

class DimensionLevelAttributeAdmin(NestedModelAdmin):
    inlines = [AnnotationNestedStackedInline]
    fields = (
        ('dataset', 'group', 'key'), 
        'attribute',
        ('code_value', 'string_value')
    )

class ObservationAdmin(NestedModelAdmin):
    inlines = [AnnotationNestedStackedInline]
    fields = (
        'dataset', 
        'series',
        'measure',
        'time',
        'obs_value'
    )

class ObservationAttributeAdmin(NestedModelAdmin):
    inlines = [AnnotationNestedStackedInline,]
    fields = (
        'obs', 
        'attribute',
        ('code_value', 'string_value')
    )

class TimeAdmin(admin.ModelAdmin):
    fields = ('datetime', 'string_time')
