from nested_admin import NestedStackedInline
from ..models import Annotation
from .common import DescriptionNestedTabularInline

class AnnotationNestedStackedInline(NestedStackedInline):
    classes = ['collapse']
    model = Annotation
    extra = 1
    fieldsets = (
        ('Identification', {
            'fields': (
                ('id_code', 'annotation_type'),
                ('annotation_title', 'annotation_URL'),
            ),
            'classes': ('collapse',)
        }),
    )
    inlines = [DescriptionNestedTabularInline]
