from django.db import models
from hvad.models import TranslatedFields

from ..models import NameableArtefact 
from common.models import Reference

#Dataflow Structure
class Dataflow(NameableArtefact):
    structure = models.ForeignKey(Reference, null=True, blank=True, related_name='+')
    translations = TranslatedFields()
