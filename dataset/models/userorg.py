
from .abstract import BaseDataset
from .org import OrgAuth
from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField
from structure.models import Concept
from structure.codelist.models import Code
from django.contrib.auth.models import User

# Create your models here.

class UserOrgRel(BaseDataset):
    user = models.ForeignKey(User)
    org = models.ForeignKey(OrgAuth)
    start = models.DateTimeField()
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class UserOrgRelAuth(models.Model):
    user = models.ForeignKey(User)
    org = models.ForeignKey(OrgAuth)
    relspan = DateTimeRangeField() 
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class UserOrgInfo(BaseDataset):
    userorg = models.ForeignKey(UserOrgRelAuth)
    start = models.DateTimeField()
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class UserOrgInfoAuth(models.Model):
    userorg = models.ForeignKey(UserOrgRelAuth)
    measurespan = DateTimeRangeField() 
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)
