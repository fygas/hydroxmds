from django.conf import settings
from django.db import models
from django.urls import reverse

from common.models import AnnotableArtefact 
from common.validators import re_validators 
from hybrid.models import Organisation


# Abstract models
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

class Item(NameableArtefact):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        unique=True,
    )
    name = models.CharField(max_length=settings.MAX_LENGTH)

    class Meta:
        abstract = True


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

class ItemScheme(MaintainableArtefact):
    #isPartial = models.BooleanField(default=False)

    class Meta(MaintainableArtefact.Meta):
        abstract = True

    def get_absolute_url(self):
        return reverse('%s:%sList' % (self.__class__._meta.app_label,  \
                                      self.__name__))

# class ItemSchemeMap(MaintainableArtefact):
#     class Meta:
#         abstract = True
#     Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
#     Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)

# class ItemAssociation(ItemSchemeMap):
#     class Meta:
#         abstract = True
