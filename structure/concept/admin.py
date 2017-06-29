from django.contrib import admin

from ..admin import ItemAdmin, ItemSchemeAdmin
from .models import ConceptScheme

class ConceptAdmin(ItemAdmin):
    extra = ['conceptScheme', 'parent', 'coreRepresentation', 'iSOConceptReference']

admin.site.register(ConceptScheme, ItemSchemeAdmin)
