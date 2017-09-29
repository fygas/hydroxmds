from django.contrib.auth.models import User 
from django.db import models

from .abstract import NameableArtefact
from ..settings import api_maxlen_settings as maxlengths 
from ..validators import re_validators as revalids

class Organisation(NameableArtefact):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[revalids['NCNameIDType']],
                               unique=True)
    name = models.CharField(max_length=maxlengths.NAME)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s:%s' % (self.id_code, self.name)

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    department = models.CharField(max_length=maxlengths.DEPARTMENT, blank=True)
    role = models.CharField(max_length=maxlengths.ROLE, blank=True)

    def __str__(self):
        return '%s: %s' % (self.user, self.organisation)

class MultiValue(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ['contact', 'value']

class Telephone(MultiValue):
    value = models.CharField('phone', max_length=maxlengths.TELEPHONE)

class Fax(MultiValue):
    value = models.CharField('FAX', max_length=maxlengths.TELEPHONE)

    class Meta:
        verbose_name_plural = 'Faxes'

class X400(MultiValue):
    value = models.CharField('X400', max_length=maxlengths.X400)

class URI(MultiValue):
    value = models.URLField('URI')

class Email(MultiValue):
    value = models.EmailField('email address')

    class Meta:
        verbose_name_plural = 'email addresses'
