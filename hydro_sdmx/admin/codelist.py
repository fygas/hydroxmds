from django.contrib import admin
from .base import ItemStackedInline, MaintainableArtefactAdmin, IdentifiableArtefactAdmin
from ..models.codelist import Code 

# class CodeTabularInline(ItemTabularInline):
#     model = Code

class CodeStackedInline(ItemStackedInline):
    model = Code

class CodelistAdmin(MaintainableArtefactAdmin):
    inlines = [CodeStackedInline]

class TextFormatInfoAdmin(admin.ModelAdmin):
    search_fields = ['id_code', 'name', 'text_type']
    list_display = ('id_code', 'name', 'text_type')
    list_display_links = ('id_code',)
    fieldsets = [ 
        (None, {
            'fields': (('id_code', 'name', 'text_type'),),
        }),
        ('Additional information', {
            'fields': (('start_value', 'end_value'),
                       ('time_interval', 'start_time', 'end_time'), 
                       ('min_length', 'max_length'),
                       ('min_value', 'max_value'),
                       'decimals',
                       'pattern',
                       'is_multiLingual'),
            'classes': ('collapse',)
        }),
    ] 

class RepresentationAdmin(IdentifiableArtefactAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] = ('id_code', 
                                     'text_format',
                                     ('enumeration', 'enumeration_format')
                                    ) 
        return fieldsets 
