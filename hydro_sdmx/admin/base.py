from django.contrib import admin
from ..forms import RegistrationForm 

class AnnotableArtefactAdmin(admin.ModelAdmin):
    filter_horizontal = ('annotations',)
    list_display = ('id',)

class IdentifiableArtefactAdmin(AnnotableArtefactAdmin):
    search_fields = ['id_code']
    list_display = ('id_code',)
    list_display_links = ('id_code',)

class StructureItemAdmin(IdentifiableArtefactAdmin):
    filter_horizontal = ('annotations', )
    search_fields = ['wrapper', 'id_code', 'concept']
    list_display = ('id_code', 'concept')
    list_display_links = ('id_code',)
    list_filter = ('wrapper',)

class NameableArtefactAdmin(IdentifiableArtefactAdmin):
    search_fields = ['id_code', 'name']
    list_display = ('id_code', 'name')
    list_display_links = ('id_code', 'name')

class ItemAdmin(NameableArtefactAdmin):
    search_fields = ['wrapper', 'id_code', 'name']
    list_display = ('id_code', 'name')
    list_display_links = ('id_code',)
    list_filter = ('wrapper',)

class VersionableArtefactAdmin(NameableArtefactAdmin):
    search_fields = ['id_code', 'name', 'version']
    list_display = ('id_code', 'name', 'version')
    list_display_links = ('id_code',)
    list_filter = ('version',)

class MaintainableArtefactAdmin(IdentifiableArtefactAdmin):
    search_fields = ['id_code', 'name', 'version', 'agency']
    list_display = ('id_code', 'name', 'version', 'agency')
    list_display_links = ('id_code',)
    list_filter = ('agency', 'version',)
    form = RegistrationForm
