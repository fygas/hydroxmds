from django.contrib import admin
from ..models import Telephone, Fax, X400, Email, URI

class InfoInline(admin.TabularInline):
    classes = ['collapse']

class TelephoneInline(InfoInline):
    model = Telephone

class FaxInline(InfoInline):
    model = Fax 

class X400Inline(InfoInline):
    model = X400 

class URIInline(InfoInline):
    model = URI 

class EmailInline(InfoInline):
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
