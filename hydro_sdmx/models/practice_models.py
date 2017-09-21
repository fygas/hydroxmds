from .abstract_postorg import MaintainableArtefact

from ..validators import re_validators 
from django.conf import settings
from django.db import models
from treebeard.mp_tree import MP_Node

class NodeCodelist(MaintainableArtefact, MP_Node):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['NCNameIDType']], \
    )
    
    node_order_by = ['id_code']
