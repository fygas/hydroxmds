from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
    fields = ('action',
              ('sdmx_file', 'sdmx_location'),
              'parent',
             )
    list_filter = ('registrant', 'action', 'interactive')
    search_fields = ('registrant', 'action', 'interactive')
    list_display = ('registrant', 'action', 'interactive')
