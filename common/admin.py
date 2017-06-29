from django.contrib import admin
from .models import Annotation

class AnnotationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Annotation, AnnotationAdmin)

