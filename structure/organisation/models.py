from django.contrib.postgres.fields import ArrayField
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

from ..constants import Organisation_types 
from common.constants import max_length

from ..models import NameableArtefact 

#Organisation Structure
class Organisation(NameableArtefact):
    type_code = models.CharField(max_length=max_length['id'], null=True, blank=True, choices=Organisation_types) 
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    Contacts = models.ManyToManyField('Contact')
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
