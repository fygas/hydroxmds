
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from treebeard.mp_tree import MP_Node

from ..settings import api_maxlen_settings as maxlengths
from ..constants import ACTIONS 

def sdmx_upload_path(instance, filename):
    return 'sdmx_uploads/user_{0}_{1}'.format(instance.user.id, filename)

class Source(models.Model):
    from_file = models.FileField(upload_to = sdmx_upload_path, blank=True, null=True)
    from_url = models.URLField(blank=True, null=True, unique=True)
    url_file = models.FileField(upload_to = sdmx_upload_path, blank=True, null=True)

class Registration(MP_Node):
    created_by = models.ForeignKey(
        User, verbose_name=_("created by"), null=True, editable=False, related_name='+' 
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=maxlengths.ID_CODE, choices=ACTIONS)
    interactive = models.BooleanField(default=False)
    set_id = models.CharField(max_length=maxlengths.ID_CODE, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s:%s:%s' % (self.created_by, self.action, self.interactive)

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)
