from django.contrib import admin
from .annotation import AnnotationInline

class IdentifiableArtefactAdmin(admin.ModelAdmin):
    search_fields = ['id_code']
    list_display = ('id_code',)
    list_display_links = ('id_code',)
    fieldsets = [ 
        (None, {
            'fields': ('id_code',),
        }),
        ('Additional information', {
            'fields': ('uri',),
            'classes': ('collapse',)
        }),
    ] 
    inlines = [AnnotationInline,]

class NameableArtefactAdmin(IdentifiableArtefactAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'name',),
            )
        }),
        ('Additional information', {
            'fields': (
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ] 
    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        search_fields.append('name')
        return search_fields

    def get_list_display(self, request):
        display = super().get_list_display(request)
        return display + ('name',)

class VersionableArtefactAdmin(NameableArtefactAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'name',),
                'version',
            )
        }),
        ('Additional information', {
            'fields': (
                ('valid_from', 'valid_to'), 
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ] 

    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        search_fields.append('version')
        return search_fields

class MaintainableArtefactAdmin(VersionableArtefactAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                ('id_code', 'name',),
                ('agency', 'version',),
            )
        }),
        ('Additional information', {
            'fields': (
                ('valid_from', 'valid_to'), 
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ] 
    list_filter = ['version', 'agency']

class ItemAdmin(NameableArtefactAdmin):
    # actions = None
    # list_display_links = None
    list_filter = ['wrapper']
    fieldsets = [ 
        (None, {
            'fields': (
                'wrapper',
                ('id_code', 'name',),
            )
        }),
        ('Additional information', {
            'fields': (
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ] 

    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        search_fields.append('wrapper__id_code')
        return search_fields

class RepresentedItemAdmin(ItemAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                'wrapper',
                ('id_code', 'name',),
            )
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            )
        }),
        ('Optional Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multiLingual'),
            'classes': ('collapse',)
        }),
        ('Additional information', {
            'fields': (
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ]
     
class ItemWithParentAdmin(ItemAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                'wrapper',
                ('id_code', 'name',),
            )
        }),
        ('Additional information', {
            'fields': (
                'parent',
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ] 

class RepresentedItemWithParentAdmin(ItemAdmin):
    fieldsets = [ 
        (None, {
            'fields': (
                'wrapper',
                ('id_code', 'name',),
            )
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            )
        }),
        ('Optional Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multiLingual'),
            'classes': ('collapse',)
        }),
        ('Additional information', {
            'fields': (
                'parent',
                ('description', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ]

# class ItemCompTabularInline(admin.TabularInline):
#     classes = ['collapse']
#
# class ItemCompBaseStackedInline(admin.StackedInline):
#     classes = ['collapse']
#
# class ItemStackedInline(ItemCompBaseStackedInline):
#     fieldsets = [ 
#         (None, {
#             'fields': (('id_code', 'name'),),
#         }),
#         ('Additional information', {
#             'fields': (('description', 'uri',),),
#             'classes': ('collapse',)
#         }),
#     ] 
#
# class ComponentStackedInline(ItemCompBaseStackedInline):
#     fieldsets = [ 
#         (None, {
#             'fields': (
#                 ('id_code', 'concept'),
#                 'representation',
#             ),
#         }),
#     ] 


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
