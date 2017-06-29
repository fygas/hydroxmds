from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from common.validators import re_validators
from django.urls import reverse

from structure.models import ItemScheme, Item

class Codelist(ItemScheme):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['NCNameIDType']], \
    )

    def get_absolute_url(self):
        return reverse('structure:codelist:codelist-index')

class Code(Item):
    codelist = models.ForeignKey(Codelist, on_delete=models.CASCADE, related_name='codes')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        unique_together = ('codelist', 'id_code')

    def clean(self):
        if self.parent:
            if self.codelist != self.parent.codelist:
                raise ValidationError({
                    'parent': ValidationError(
                        _('''Parent and child codes must belong in the \
                            same Codelist'''), code='local'
                    ),
                })
