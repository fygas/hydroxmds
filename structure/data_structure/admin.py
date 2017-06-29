from django.contrib import admin

from .models import DataStructure, DataStructureComponent, DataStructureComponentGroup

class DataStructureAdmin(admin.ModelAdmin):
    pass

class DataStructureComponentAdmin(admin.ModelAdmin):
    pass

class DataStructureComponentGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(DataStructure, DataStructureAdmin)
admin.site.register(DataStructureComponent, DataStructureComponentAdmin)
admin.site.register(DataStructureComponentGroup, DataStructureComponentGroupAdmin)
