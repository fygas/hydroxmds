from django.contrib.contenttypes.models import ContentType
from django.db import models

class ReferenceObject(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return 'object: %s, id: %s' % (self.content_type, self.object_id)
