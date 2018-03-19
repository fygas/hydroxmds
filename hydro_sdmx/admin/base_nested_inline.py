from .annotation import AnnotationNestedStackedInline 
from .common import DescriptionNestedTabularInline, NameNestedTabularInline
from nested_admin import NestedStackedInline 

class ItemNestedStackedInline(NestedStackedInline):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline]
    classes = ['collapse']
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri'),
            ),
            'classes': ('collapse',)
        }),
    ] 

class RepresentedItemNestedStackedInline(ItemNestedStackedInline):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri'),
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

class ItemWithParentNestedStackedInline(ItemNestedStackedInline):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri', 'parent'),
            ),
            'classes': ('collapse',)
        }),
    ] 

class RepresentedItemWithParentNestedStackedInline(RepresentedItemNestedStackedInline):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri', 'parent'),
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
