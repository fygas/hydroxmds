from nested_admin import NestedTabularInline 
from ..models import Name, Description 

class DescriptionNestedTabularInline(NestedTabularInline):
    classes = ('collapse', )
    model = Description 
    extra = 1
    fields = ('lang', 'text')
    verbose_name_plural = 'Multilingual Description'
    verbose_name = 'description'

class NameNestedTabularInline(NestedTabularInline):
    classes = ('collapse', )
    model = Name
    extra = 1
    fields = ('lang', 'text')
    verbose_name_plural = 'Multilingual Name'
    verbose_name = 'name'
