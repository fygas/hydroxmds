from django.contrib import admin
from hvad.admin import TranslatableAdmin
from django.utils.translation import ugettext as _

from structure.admin import ItemAdmin, ItemSchemeAdmin
from .models import OrganisationScheme, Organisation, Contact

class OrganisationAdmin(ItemAdmin):
    extra = ['organisationScheme', 'parent']

class ContactAdmin(TranslatableAdmin):
    change_form_template = 'sdmx/admin/change_form.html'
    #form = ContactAdminForm

    def get_fieldsets(self, request, obj=None):
        return (
            (_('Common fields'), {
                'fields': (
                    'id_code', 'organisation', 'telephone', 'fax', 'x400', \
                    'uRI', 'email',  
                )
            }),
            (_('Translated fields'), {
                'fields': ('name', 'department', 'role')
            })
        )

admin.site.register(OrganisationScheme, ItemSchemeAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Contact, ContactAdmin)
