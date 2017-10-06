from django.db import models

from .abstract import ItemWithParent, MaintainableArtefact

from ..settings import api_maxlen_settings 
from ..validators import re_validators 


#Concrete models
class Codelist(MaintainableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE, \
        validators=[re_validators['NCNameIDType']], \
    )

class Code(ItemWithParent):
    wrapper = models.ForeignKey(Codelist, verbose_name='Codelist', on_delete=models.CASCADE, related_name='codes')
