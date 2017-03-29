from django.contrib import admin
from hvad.admin import TranslatableAdmin
from django.utils.translation import ugettext as _
from .models import Annotation

class AnnotationAdmin(TranslatableAdmin):
    change_form_template = 'sdmx/admin/change_form.html'

    def get_fieldsets(self, request, obj=None):
        return (
            (_('Common fields'), {
                'fields': (
                    'annotationTitle', 'annotationType', 'annotationURL', \
                    'id_code'
                )
            }),
            (_('Translated fields'), {
                'fields': ('annotationText', )
            })
        )

admin.site.register(Annotation, AnnotationAdmin)

