from django.conf import settings
from django.db import models

from ..validators import re_validators 
from org.models import Organisation

# Abstract models

# The following is concrete that is used in AnnotableArtefact abtract
# model 

class Annotation(models.Model):
    annotation_title = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True)
    annotation_type = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True)
    annotation_URL = models.URLField(null=True, blank=True)
    annotation_text = models.TextField(null=True, blank=True)
    id_code = models.CharField('id', max_length=settings.MAX_LENGTH, null=True, blank=True)

    def __str__(self):
        display_name = '%(id_code)s: %(title)s' % \
                {'title': self.annotation_title, 'id_code': self.id_code}
        return display_name

# Abstract models
class AnnotableArtefact(models.Model):
    annotations = models.ManyToManyField(Annotation, related_name='+', blank=True)

    class Meta:
        abstract = True


class IdentifiableArtefact(AnnotableArtefact):
    uri = models.URLField(null=True, blank=True)
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        null=True, blank=True,
    )


    class Meta:
        abstract = True

    def __str__(self):
        return self.id_code

class NameableArtefact(IdentifiableArtefact):
    name = models.CharField(
        max_length=settings.MAX_LENGTH, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name 

class VersionableArtefact(NameableArtefact):
    version = models.CharField(
        max_length=settings.MAX_LENGTH, \
        validators=[re_validators['VersionType']], default='1.0'
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class MaintainableArtefact(VersionableArtefact):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
    )
    agency = models.ForeignKey(Organisation, on_delete=models.CASCADE) 
    is_final= models.BooleanField(default=False)
    name = models.CharField(max_length=settings.MAX_LENGTH)

    class Meta:
        unique_together = ('id_code', 'agency', 'version')
        abstract = True
