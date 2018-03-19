from .annotation import AnnotationNestedStackedInline 
from .base import ItemWithParentAdmin, MaintainableArtefactAdmin
from .base_nested_inline import ItemWithParentNestedStackedInline
from .common import NameNestedTabularInline, DescriptionNestedTabularInline

from ..models.codelist import Code 

class CodeNestedStackedInline(ItemWithParentNestedStackedInline):
    model = Code
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline,]

class CodelistAdmin(MaintainableArtefactAdmin):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline, CodeNestedStackedInline]

class CodeAdmin(ItemWithParentAdmin):
    pass
