from django.db import models

from ..settings import api_maxlen_settings

class Annotation(models.Model):
    annotation_title = models.CharField(max_length=api_maxlen_settings.ANNOTATION_TITLE, blank=True, db_index=True)
    annotation_type = models.CharField(max_length=api_maxlen_settings.ANNOTATION_TYPE, blank=True)
    annotation_URL = models.URLField(null=True, blank=True)
    annotation_text = models.TextField(blank=True)
    id_code = models.CharField('id', max_length=api_maxlen_settings.ID_CODE, blank=True, db_index=True)

    def __str__(self):
        return 'id: %s, id_code: %s, title: %s' % (self.id, self.id_code, self.annotation_title)

    class Meta:
        ordering = ['id_code', 'annotation_title', 'annotation_text']
        index_together = ['id_code', 'annotation_title']
