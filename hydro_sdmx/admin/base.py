from django.contrib import admin

class AnnotableArtefactAdmin(admin.ModelAdmin):
    filter_horizontal = ('annotations',)
    list_display = ('id',)

class IdentifiableArtefactAdmin(AnnotableArtefactAdmin):
    search_fields = ['id_code']
    list_display = ('id_code',)
    list_display_links = ('id_code',)
    fieldsets = (
        (None, {
            'fields': ('id_code',),
        }),
        ('Additional information', {
            'fields': ('description', ('parent', 'uri'), 'annotations'),
            'classes': ('collapse',)
        }),
    )

class NameableArtefactAdmin(IdentifiableArtefactAdmin):

    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        search_fields.append('name')
        return search_fields

    def get_list_display(self, request):
        display = super().get_list_display(request)
        return display + ('name',)

    def get_list_display_links(self, request, obj=None):
        display = super().get_list_display_links(request, obj)
        return display + ('name',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] = (('id_code', 'name'),) 
        return fieldsets 

# from django.contrib import admin
# from ..forms import RegistrationForm 
#
# class AnnotableArtefactAdmin(admin.ModelAdmin):
#     filter_horizontal = ('annotations',)
#     list_display = ('id',)
#
# class IdentifiableArtefactAdmin(AnnotableArtefactAdmin):
#     search_fields = ['id_code']
#     list_display = ('id_code',)
#     list_display_links = ('id_code',)
#
# class StructureItemAdmin(IdentifiableArtefactAdmin):
#     filter_horizontal = ('annotations', )
#     search_fields = ['wrapper', 'id_code', 'concept']
#     list_display = ('id_code', 'concept')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)
#
# class NameableArtefactAdmin(IdentifiableArtefactAdmin):
#     search_fields = ['id_code', 'name']
#     list_display = ('id_code', 'name')
#     list_display_links = ('id_code', 'name')
#
# class ItemAdmin(NameableArtefactAdmin):
#     search_fields = ['wrapper', 'id_code', 'name']
#     list_display = ('id_code', 'name')
#     list_display_links = ('id_code',)
#     list_filter = ('wrapper',)
#
# class VersionableArtefactAdmin(NameableArtefactAdmin):
#     search_fields = ['id_code', 'name', 'version']
#     list_display = ('id_code', 'name', 'version')
#     list_display_links = ('id_code',)
#     list_filter = ('version',)
#
# class MaintainableArtefactAdmin(IdentifiableArtefactAdmin):
#     search_fields = ['id_code', 'name', 'version', 'agency']
#     list_display = ('id_code', 'name', 'version', 'agency')
#     list_display_links = ('id_code',)
#     list_filter = ('agency', 'version',)
#     form = RegistrationForm
