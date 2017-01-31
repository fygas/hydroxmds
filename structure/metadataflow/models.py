from django.db import models
from hvad.models import TranslatedFields

from ..models import NameableArtefact 
from common.models import Reference

class Metadataflow(NameableArtefact):
    structure = models.ForeignKey(Reference, null=True, blank=True)
    translations = TranslatedFields()
