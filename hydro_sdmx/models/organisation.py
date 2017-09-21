from django.contrib.auth.user import User
from django.db import models

from .abstract import NameableArtefact, Item
from ..settings import api_maxlen_settings
from ..validators import re_validators

class Organisation(NameableArtefact):
    id_code = models.CharField(
        'id', 
        max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['NCNameIDType']],
        unique=True
    )
    name = models.CharField(max_length=api_maxlen_settings.NAME)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

class Contact(Item):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wrapper = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    department = models.CharField(max_length=api_maxlen_settings.DEPARTMENT, blank=True)
    role = models.CharField(max_length=api_maxlen_settings.ROLE, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id_code']),
            models.Index(fields=['name']),
            models.Index(fields=['id_code', 'name']),
        ]

    def __str__(self):
        return 'id_code: %s, name: %s' % (self.id_code, self.name)

class MultiValue(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ['contact', 'value']

class Telephone(MultiValue):
    value = models.CharField(max_length=api_maxlen_settings.TELEPHONE)

class Fax(MultiValue):
    value = models.CharField(max_length=api_maxlen_settings.TELEPHONE)

class X400(MultiValue):
    value = models.CharField(max_length=api_maxlen_settings.X400)

class URI(MultiValue):
    value = models.URLField()

class Email(MultiValue):
    value = models.EmailField()
