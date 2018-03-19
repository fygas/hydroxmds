from nested_admin import NestedTabularInline, NestedStackedInline 

from .annotation import AnnotationNestedStackedInline
from .base import NameableArtefactAdmin, MaintainableArtefactAdmin
from .common import NameNestedTabularInline, DescriptionNestedTabularInline
from ..models import Telephone, Fax, X400, Email, URI, Contact

class TelephoneNestedTabularInline(NestedTabularInline):
    model = Telephone

class FaxNestedTabularInline(NestedTabularInline):
    model = Fax 

class X400NestedTabularInline(NestedTabularInline):
    model = X400 

class URINestedTabularInline(NestedTabularInline):
    model = URI 

class EmailNestedTabularInline(NestedTabularInline):
    model = Email 

class DepartmentNestedTabularInline(NameNestedTabularInline):
    fk_name = 'contact_department'
    verbose_name_plural = 'Departments'

class RoleNestedTabularInline(NameNestedTabularInline):
    fk_name = 'contact_role'
    verbose_name_plural = 'Roles'
    
class ContactNameNestedTabularInline(NameNestedTabularInline):
    fk_name = 'contact_name'
    verbose_name_plural = 'Names'

class ContactNestedStackedInline(NestedStackedInline):
    model = Contact
    classes = ('collapse', )
    inlines = [
        ContactNameNestedTabularInline, DepartmentNestedTabularInline,
        RoleNestedTabularInline, TelephoneNestedTabularInline,
        EmailNestedTabularInline, FaxNestedTabularInline,
        X400NestedTabularInline, URINestedTabularInline,
        AnnotationNestedStackedInline
    ]
    fieldsets = (
        (None, {
            'fields': (('user', 'organisation',)),
        }),
    )

class OrganisationAdmin(NameableArtefactAdmin):
    inlines = [NameNestedTabularInline, DescriptionNestedTabularInline, AnnotationNestedStackedInline, ContactNestedStackedInline]
    filter_horizontal = ('schemes',)
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'uri',),
                'parent',
                'schemes',
            ),
            'classes': ('collapse',)
        }),
    ]

class OrganisationSchemeAdmin(MaintainableArtefactAdmin):
    pass
