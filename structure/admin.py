from django.contrib import admin
from .models import (
    TextFormatInfo, Representation, ConceptTag, ConceptScheme, Concept
)

class NameableAdmin(admin.ModelAdmin):
    search_fields = ['id_code', 'name']
    filter_horizontal = ['annotations']

class ItemSchemeAdmin(NameableAdmin):
    pass

class ItemAdmin(NameableAdmin):
    pass

class TextFormatInfoAdmin(admin.ModelAdmin):
    pass

class RepresentationAdmin(admin.ModelAdmin):
    pass

class ConceptTagAdmin(NameableAdmin):
    pass

class ConceptSchemeAdmin(NameableAdmin):
    pass

class ConceptAdmin(admin.ModelAdmin):
    search_fields = ['concept_tag__id_code', 'concept_tag__name']

admin.site.register(TextFormatInfo, TextFormatInfoAdmin)
admin.site.register(Representation, RepresentationAdmin)
admin.site.register(ConceptTag, ConceptAdmin)
admin.site.register(ConceptScheme, ConceptSchemeAdmin)
admin.site.register(Concept, ConceptAdmin)

