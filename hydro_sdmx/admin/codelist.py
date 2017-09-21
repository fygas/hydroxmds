
from django.contrib import admin

class TextFormatInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('annotations', )
    search_fields = ['id_code', 'name', 'text_type']
    list_display = ('id_code', 'name', 'text_type',)
    list_filter = ('text_type',)
