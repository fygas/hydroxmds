
from .abstract import BaseDataset
from .org import OrgAuth
from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField
from structure.models import Concept
from structure.codelist.models import Code

class Sec(BaseDataset):
    isnew = models.BooleanField()
    idcode = models.CharField(max_length=255)
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)

class SecAuth(models.Model):
    idcode = models.CharField(max_length=255)
    lifespan = DateTimeRangeField() 
    sectype = models.ForeignKey(Code)

class SecIssuer(BaseDataset):
    sec = models.ForeignKey(SecAuth)
    issuer = models.ForeignKey(OrgAuth)
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)
    
class SecIssuerAuth(models.Model):
    sec = models.ForeignKey(Sec)
    issuer = models.ForeignKey(OrgAuth)
    relspan = DateTimeRangeField() 
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class SecInfo(BaseDataset):
    sec = models.ForeignKey(Sec)
    start = models.DateTimeField()
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class SecInfoAuth(models.Model):
    sec = models.ForeignKey(Sec)
    measurespan = DateTimeRangeField() 
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class SecInfoPeriodic(BaseDataset):
    freq = models.ForeignKey(Code)
    sec = models.ForeignKey(Sec)
    period = models.CharField(max_length=255)
    measure = models.ForeignKey(Concept)
    obs_value = models.CharField(max_length=255)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)

class SecHolderSnapInfo(BaseDataset):
    freq = models.ForeignKey(Code)
    sec = models.ForeignKey(SecAuth)
    holder = models.ForeignKey(OrgAuth)
    measure = models.ForeignKey(Concept)
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)
    
class SecHolderAuth(models.Model):
    sec = models.ForeignKey(SecAuth)
    holder = models.ForeignKey(OrgAuth)
    measurespan = DateTimeRangeField() 
    measure = models.ForeignKey(Concept)
    obs_value = models.ForeignKey(Code)
    source = models.ForeignKey(Code)
    confidentiality = models.ForeignKey(Code)
