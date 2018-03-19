from django.contrib.auth.models import User
from django.db import models

from treebeard.mp_tree import MP_Node

from ..settings import api_maxlen_settings as maxlengths
from .abstract import MaintainableArtefact, IdentifiableArtefact 


class OrganisationScheme(MaintainableArtefact):
    pass

class Organisation(IdentifiableArtefact, MP_Node):
    schemes = models.ManyToManyField(OrganisationScheme, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta(IdentifiableArtefact.Meta):
        unique_together = ('id_code',)

    def __str__(self):
        return self.id_code 

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)

            return  #add_root and add_child save as well
        super().save(**kwargs)

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    department = models.CharField(max_length=maxlengths.DEPARTMENT, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['organisation']),
            models.Index(fields=['user', 'organisation']),
        ]
        unique_together = ('user', 'organisation')

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
