import uuid

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from treebeard.mp_tree import MP_Node

from ..settings import api_maxlen_settings as maxlengths
from ..constants import ACTIONS 

def sdmx_upload_path(instance, filename):
    return 'sdmx_uploads/user_{0}_{1}_{2}'.format(instance.user.id, uuid.uuid4(), filename)

class Registration(MP_Node, models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=maxlengths.ID_CODE, choices=ACTIONS, default='A')
    interactive = models.BooleanField(default=False, editable=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    sdmx_file = models.FileField(upload_to = sdmx_upload_path, blank=True, null=True)
    sdmx_location = models.URLField(blank=True, null=True)
    registrant = models.ForeignKey(
        User, verbose_name=_("registrant"), null=True, editable=False, related_name='+' 
    )

    def __str__(self):
        return '%s:%s:%s' % (self.registrant.username, self.action, self.interactive)

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)
