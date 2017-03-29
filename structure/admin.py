from hvad.admin import TranslatableAdmin
from django.utils.translation import ugettext as _

class ItemSchemeAdmin(TranslatableAdmin):
    change_form_template = 'sdmx/admin/change_form.html'

    def get_fieldsets(self, request, obj=None):
        return (
            (_('Common fields'), {
                'fields': (
                    'id_code', 'annotations', 'uri', 'version', 'validFrom', \
                    'validTo', 'agencyID', 'isFinal'
                )
            }),
            (_('Translated fields'), {
                'fields': ('name', 'description')
            })
        )


class ItemAdmin(TranslatableAdmin):
    extra = None 
    change_form_template = 'sdmx/admin/change_form.html'

    def get_fieldsets(self, request, obj=None):
        if not self.extra: self.extra = []
        return (
            (_('Common fields'), {
                'fields': ['id_code', 'annotations', 'uri'] + self.extra
            }),
            (_('Translated fields'), {
                'fields': ('name', 'description')
            })
        )
