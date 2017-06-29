from django.contrib import admin

from .models import Dataflow

class DataflowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dataflow, DataflowAdmin)
