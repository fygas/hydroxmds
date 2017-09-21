from .base import IdentifiableArtefactAdmin

class DimensionAdmin(IdentifiableArtefactAdmin):
    filter_horizontal = ('annotations', 'roles', 'groups')
    search_fields = ['wrapper', 'id_code', 'concept']
    list_display = ('id_code', 'concept')
    list_display_links = ('id_code',)
    list_filter = ('wrapper',)

class AttributeAdmin(IdentifiableArtefactAdmin):
    filter_horizontal = ('annotations', 'roles', 'attached2dims', 'attached2groups')
    search_fields = ['wrapper', 'id_code', 'concept']
    list_display = ('id_code', 'concept')
    list_display_links = ('id_code',)
    list_filter = ('wrapper',)
