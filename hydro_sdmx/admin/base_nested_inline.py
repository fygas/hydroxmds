from nested_admin import NestedStackedInline 

from .annotation import AnnotationNestedStackedInline

from .base_inline import ItemStackedInline, ItemWithParentStackedInline, RepresentedItemStackedInline, RepresentedItemWithParentStackedInline 

class ItemBaseNestedStackedInline(NestedStackedInline):
    inlines = [AnnotationNestedStackedInline]
    classes = ['collapse']

class ItemNestedStackedInline(ItemBaseNestedStackedInline, ItemStackedInline):
    pass

class RepresentedItemNestedStackedInline(ItemBaseNestedStackedInline, RepresentedItemStackedInline):
    pass

class ItemWithParentNestedStackedInline(ItemBaseNestedStackedInline, ItemWithParentStackedInline):
    pass

class RepresentedItemWithParentNestedStackedInline(ItemBaseNestedStackedInline, RepresentedItemWithParentStackedInline):
    pass
