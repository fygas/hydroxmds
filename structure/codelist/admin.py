from django.contrib import admin

from ..admin import NameableAdmin 
from .models import Codelist, Code

class CodeAdmin(NameableAdmin):
    extra = ['codelist', 'parent']

admin.site.register(Codelist)
admin.site.register(Code, CodeAdmin)
