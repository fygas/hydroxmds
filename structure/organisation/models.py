from django.db import models
from .structure_base import NameableArtefact 
from hvad.models import TranslatableModel, TranslatedFields
from django.contrib.postgres.fields import ArrayField
from common.models.constants import max_length
from .constants import Organisation_types 

#Organisation Structure
class Organisation(NameableArtefact):
    type_ = models.CharField(max_length=max_length['id'], choices=Organisation_types, null=True, blank=True)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    Contacts = models.ManyToManyField('Contact', null=True, blank=True)
    translations = TranslatedFields()

class Contact(TranslatableModel):
    translations = TranslatedFields(
        Name = models.CharField(max_length=max_length['id'], null=True, blank=True),
        Department = models.CharField(max_length=max_length['id'], null=True, blank=True),
        Role = models.CharField(max_length=max_length['id'], null=True, blank=True)
    )
    Telephone = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    Fax = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    X400 = ArrayField(models.CharField(max_length=max_length['name'], null=True, blank=True),  null=True, blank=True)
    URI = ArrayField(models.URLField(null=True, blank=True),  null=True, blank=True)
    Email = ArrayField(models.EmailField(null=True, blank=True),  null=True, blank=True)
