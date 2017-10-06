from django.contrib import admin
from .annotation import AnnotationStackedInline

class ItemBaseStackedInline(admin.StackedInline):
    inlines = [AnnotationStackedInline]
    classes = ['collapse']

class ItemStackedInline(ItemBaseStackedInline):
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

class RepresentedItemStackedInline(ItemBaseStackedInline):
    fieldsets = [ 
        (None, {
            'fields': (
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

class ItemWithParentStackedInline(ItemStackedInline):
    fieldsets = [ 
        (None, {
            'fields': (
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

class RepresentedItemWithParentStackedInline(ItemWithParentStackedInline, RepresentedItemStackedInline):
    pass
