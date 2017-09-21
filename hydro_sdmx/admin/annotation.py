from django.contrib import admin

class AnnotationAdmin(admin.ModelAdmin):
    list_filter = ('annotation_type',)
    search_fields = ('annotation_type', 'id_code', 'annotation_title')
    list_display = ('id_code', 'annotation_title', 'annotation_title')
