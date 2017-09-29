from django.contrib import admin

from .base import MaintainableArtefactAdmin
from ..models import Telephone, Fax, X400, Email, URI

class OrganisationSchemeOrganisationsAdmin(MaintainableArtefactAdmin):

    filter_horizontal = ('annotations', 'items')
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if fieldsets[1][0] == 'items':
            return fieldsets
        else:
            fieldsets.insert(1, ('items', {
                'fields': ('items',),
                'classes': ('collapse',)
            }))
            return fieldsets 
class TelephoneInline(admin.TabularInline):
    model = Telephone

class FaxInline(admin.TabularInline):
    model = Fax 

class X400Inline(admin.TabularInline):
    model = X400 

class URIInline(admin.TabularInline):
    model = URI 

class EmailInline(admin.TabularInline):
    model = Email 

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        TelephoneInline, EmailInline, FaxInline, X400Inline, URIInline 
    ]
    search_fields = ['user.username', 'user.first_name', 'user.last_name', 'organisation.id_code', 'organisation.name']
    list_display = ('user', 'organisation', 'department', 'role')
    list_display_links = ('user',)
    fieldsets = (
        (None, {
            'fields': (('user', 'organisation',),
                       ('department', 'role')),
        }),
        # ('Additional information', {
        #     'fields': ('description', ('parent', 'uri'), 'annotations'),
        #     'classes': ('collapse',)
        # }),
    )
