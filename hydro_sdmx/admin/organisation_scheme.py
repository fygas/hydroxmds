# from nested_admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin
#
# from .annotation import AnnotationNestedStackedInline
# from .base import NameableArtefactAdmin
# from ..models import Telephone, Fax, X400, Email, URI, Contact
#
#
# class TelephoneNestedTabularInline(NestedTabularInline):
#     model = Telephone
#
# class FaxNestedTabularInline(NestedTabularInline):
#     model = Fax 
#
# class X400NestedTabularInline(NestedTabularInline):
#     model = X400 
#
# class URINestedTabularInline(NestedTabularInline):
#     model = URI 
#
# class EmailNestedTabularInline(NestedTabularInline):
#     model = Email 
#
# class ContactNestedStackedInline(NestedStackedInline):
#     model = Contact
#     inlines = [
#         TelephoneNestedTabularInline, EmailNestedTabularInline, FaxNestedTabularInline, X400NestedTabularInline, URINestedTabularInline, AnnotationNestedStackedInline
#     ]
#     fieldsets = (
#         (None, {
#             'fields': (('user', 'organisation',),
#                        ('department', 'role')),
#         }),
#     )
#
# class OrganisationAdmin(NestedModelAdmin, NameableArtefactAdmin):
#     inlines = [ContactNestedStackedInline, AnnotationNestedStackedInline]
#     filter_horizontal = ('schemes',)
#     fieldsets = [ 
#         (None, {
#             'fields': (
#                 ('id_code', 'name',),
#                 'schemes',
#             )
#         }),
#         ('Additional information', {
#             'fields': (
#                 'parent',
#                 ('description', 'uri',),
#             ),
#             'classes': ('collapse',)
#         }),
#     ]
