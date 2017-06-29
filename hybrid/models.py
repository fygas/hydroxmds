from django.conf import settings
from django.db import models
from common.validators import re_validators 
from django.urls import reverse

# Create your models here.

class Organisation(models.Model):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        unique=True
    )
    alias = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('hybrid:org-list')

    def __str__(self):
        return self.id_code

class Contact(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
    )
    class Meta:
        unique_together = ['organisation', 'id_code']
