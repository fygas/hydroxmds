
from django.db import models
from django.utils.translation import ugettext as _

from treebeard.mp_tree import MP_Node

from ..settings import api_maxlen_settings
from ..constants import ACTIONS 

def sdmx_upload_path(instance, filename):
    return 'sdmx_uploads/user_{0}_{1}'.format(instance.user.id, filename)

class Source(models.Model):
    from_file = models.FileField(upload_to = sdmx_upload_path, blank=True, null=True, unique=True)
    from_url = models.URLField(blank=True, null=True, unique=True)

class BaseRegistration(models.Model, MP_Node):
    created_by = models.ForeignKey(
        'contact', verbose_name=_("created by"), null=True, editable=False, related_name='+' 
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(choices=ACTIONS)
    interactive = models.BooleanField(default=False)
    set_id = models.CharField(min_length=api_maxlen_settings.ID_CODE, null=True, blank=True)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s-%s_%s' % (self.created_by, self.action, self.interactive)

    def save(self, **kwargs):
        from ..utils.permissions import get_current_user
        self.created_by = get_current_user()
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)

# class TrakingModel(models.Model):
#     created_by = models.ForeignKey(
#         'auth.User', verbose_name=_("created by"), null=True, editable=False, related_name='+' 
#     )
#     changed_by = models.ForeignKey(
#         'auth.User', verbose_name=_("changed by"), null=True, editable=False, related_name='+'
#     )
#     creation_date = models.DateTimeField(auto_now_add=True)
#     changed_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
#     def save(self, commit=True, **kwargs):
#         """
#         Args:
#             commit: True if model should be really saved
#         """
#         created = not bool(self.pk)
#         from ..utils.permissions import get_current_user
#
#         user = get_current_user()
#
#         if user:
#             self.changed_by = user 
#
#         if created:
#             self.created_by = self.changed_by
#
#         if commit:
#             super().save(**kwargs)

class Dataset(BaseRegistration):
    pass

class Metadataset(BaseRegistration):
    pass

class MetaStructure(BaseRegistration):
    pass

