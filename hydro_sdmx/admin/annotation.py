from django.contrib import admin
from nested_admin import NestedStackedInline
from ..models import Annotation

class AnnotationStackedInline(admin.StackedInline):
    classes = ['collapse']
    model = Annotation
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('annotation_text',),
        }),
        ('Additional info', {
            'fields': (
                ('id_code', 'annotation_type'),
                ('annotation_title', 'annotation_URL'),
            ),
            'classes': ('collapse',)
        }),
    )

class AnnotationNestedStackedInline(NestedStackedInline, AnnotationStackedInline):
    pass
