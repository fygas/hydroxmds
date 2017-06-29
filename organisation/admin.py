from django.contrib import admin

from structure.admin import ItemSchemeAdmin
from .models import OrganisationScheme

admin.site.register(OrganisationScheme, ItemSchemeAdmin)
