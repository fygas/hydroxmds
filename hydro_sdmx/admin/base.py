from .annotation import AnnotationNestedStackedInline
from .common import NameNestedTabularInline, DescriptionNestedTabularInline
from nested_admin import NestedModelAdmin

class IdentifiableArtefactAdmin(NestedModelAdmin):
    search_fields = ['id_code']
    list_display = ('id_code',)
    list_display_links = ('id_code',)
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri',),
            ),
            'classes': ('collapse',)
        }),
    ]
    inlines = [AnnotationNestedStackedInline,]

class NameableArtefactAdmin(IdentifiableArtefactAdmin):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline,]

    # # TODO FIX with international name
    # def get_search_fields(self, request):
    #     search_fields = super().get_search_fields(request)
    #     search_fields.append('name')
    #     return search_fields
    #
    # def get_list_display(self, request):
    #     display = super().get_list_display(request)
    #     return display + ('name',)

class VersionableArtefactAdmin(NameableArtefactAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'version',),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Duration', {
            'fields': (
                ('valid_from', 'valid_to'), 
            ),
            'classes': ('collapse',)
        }),
    ] 

    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        search_fields.append('version')
        return search_fields

class MaintainableArtefactAdmin(VersionableArtefactAdmin):
    raw_id_fields = ('agency',)
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'agency', 'version'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Duration', {
            'fields': (
                ('valid_from', 'valid_to'), 
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
        ('Identification', {
            'fields': (
                ('wrapper', 'id_code'),
                'uri',
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
        ('Identification', {
            'fields': (
                ('wrapper', 'id_code'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('More Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multi_lingual'),
            'classes': ('collapse',)
        }),
    ]
     
class ItemWithParentAdmin(ItemAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('wrapper', 'id_code', 'parent'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
    ] 

class RepresentedItemWithParentAdmin(ItemAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('wrapper', 'id_code', 'parent'),
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Representation', {
            'fields': (
                ('enumeration', 'text_type',),
            ),
            'classes': ('collapse',)
        }),
        ('More Representation', {
            'fields': (
                ('start_value', 'end_value'),
                ('time_interval', 'start_time', 'end_time'), 
                ('min_length', 'max_length'),
                ('min_value', 'max_value'),
                'decimals',
                'pattern',
                'is_multi_lingual'),
            'classes': ('collapse',)
        }),
    ]
