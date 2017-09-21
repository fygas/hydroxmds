from django.contrib import admin

from .forms import RegistrationForm 

class RegistrationAdmin(admin.ModelAdmin):
    list_filter = ('created_by', 'action', 'interactive')
    search_fields = ('created_by', 'action', 'interactive')
    list_display = ('created_by', 'actions', 'interactive')
    form = RegistrationForm
