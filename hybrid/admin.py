from django.contrib import admin
from .models import Organisation

# Register your models here.

class OrganisationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organisation, OrganisationAdmin)
