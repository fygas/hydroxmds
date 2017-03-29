from django.contrib import admin

from ..admin import ItemAdmin, ItemSchemeAdmin
from .models import Codelist, Code

class CodeAdmin(ItemAdmin):
    extra = ['codelist', 'parent']

admin.site.register(Codelist, ItemSchemeAdmin)
admin.site.register(Code, CodeAdmin)

