from nested_admin import NestedModelAdmin

from .annotation import AnnotationNestedStackedInline 
from .base import ItemWithParentAdmin, MaintainableArtefactAdmin
from .base_nested_inline import ItemWithParentNestedStackedInline
from ..models.codelist import Code 

class CodeNestedStackedInline(ItemWithParentNestedStackedInline):
    model = Code
    inlines = [AnnotationNestedStackedInline,]

class CodelistAdmin(NestedModelAdmin, MaintainableArtefactAdmin):
    inlines = [CodeNestedStackedInline, AnnotationNestedStackedInline]

class CodeAdmin(ItemWithParentAdmin):
    pass

# class TextFormatNestedStackedBaseInline(NestedStackedInline):
#     model = TextFormat
#     fieldsets = [ 
#         (None, {
#             'fields': ('text_type',),
#         }),
#         ('Additional information', {
#             'fields': (('start_value', 'end_value'),
#                        ('time_interval', 'start_time', 'end_time'), 
#                        ('min_length', 'max_length'),
#                        ('min_value', 'max_value'),
#                        'decimals',
#                        'pattern',
#                        'is_multiLingual'),
#             'classes': ('collapse',)
#         }),
#     ] 
#
# class TextFormatNestedStackedInline(TextFormatNestedStackedBaseInline):
#     fk_name = 'text_format'
#
# class EnumerationFormatNestedStackedInline(TextFormatNestedStackedBaseInline):
#     fk_name = 'enumeration_format'
#
# class RepresentationNestedStackedInline(NestedStackedInline):
#     model = Representation 
#     fieldsets = [ 
#         (None, {
#             'fields': ('codelist',),
#         }),
#     ] 
#     inlines = [TextFormatNestedStackedInline, EnumerationFormatNestedStackedInline]
