from django.contrib import admin

class AnnotationAdmin(admin.ModelAdmin):

    search_fields = ['id_code', 'annotation_type']
    fieldsets = (
        (None, {
            'fields': (('id_code', 'annotation_title'), 'annotation_text'),
        }),
        ('Additional info', {
            'fields': ('annotation_type', 'annotation_URL'),
            'classes': ('collapse',)
        }),
    )
