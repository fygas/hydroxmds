from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from hvad.models import TranslatedFields
from common.constants import max_length
from common.validators import re_validators

from ..models import Item, ItemScheme

class Codelist(ItemScheme):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['NCNameIDType']], \
    )
    translations = TranslatedFields()

class Code(Item):
    codelist = models.ForeignKey(Codelist, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )
    translations = TranslatedFields()

    class Meta:
        unique_together = ('codelist', 'id_code')

    def clean(self):
        if self.codelist != self.parent.codelist:
            raise ValidationError({
                'parent': ValidationError(
                    _('''Parent and child codes must belong in the \
                        same Codelist'''), code='local'
                ),
            })
