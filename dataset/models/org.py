from .abstract import BaseDataset
from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField
from structure.models import Concept
from structure.codelist.models import Code

# Create your models here.

class Org(BaseDataset):
    isnew = models.BooleanField()
    idcode = models.CharField(max_length=255)
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)

class OrgAuth(models.Model):
    idcode = models.CharField(max_length=255)
    lifespan = DateTimeRangeField() 

class OrgInfo(BaseDataset):
    idcode = models.ForeignKey(OrgAuth)
    start = models.DateTimeField()
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgInfoAuth(models.Model):
    idcode = models.ForeignKey(OrgAuth)
    attrspan = DateTimeRangeField() 
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgRel(BaseDataset):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    start = models.DateTimeField()
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgRelAuth(models.Model):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    relspan = DateTimeRangeField() 
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgOwn(BaseDataset):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    start = models.DateTimeField()
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgOwnAuth(models.Model):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    ownspan = DateTimeRangeField() 
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgEvent(BaseDataset):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    event_date = models.DateTimeField()
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class OrgEventAuth(models.Model):
    idcode = models.ForeignKey(OrgAuth)
    counter_idcode = models.ForeignKey(OrgAuth)
    event_date = models.DateTimeField()
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)
