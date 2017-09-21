from .models import (
    TextFormatInfo, Representation, ConceptScheme, Concept, Code, Codelist
)

from django.contrib import admin

class NameableAdmin(admin.ModelAdmin):
    search_fields = ['id_code', 'name']
    filter_horizontal = ['annotations']

class CodeAdmin(NameableAdmin):
    extra = ['codelist', 'parent']

class ConceptAdmin(admin.ModelAdmin):
    search_fields = ['id_code', 'name']

for model in [Codelist, TextFormatInfo, Representation, ConceptScheme]:
    admin.site.register(model)

admin.site.register(Code, CodeAdmin)
admin.site.register(Concept, ConceptAdmin)

