from django.db import models
from .structure_base import NameableArtefact 
from common.models import Reference
from hvad.models import TranslatedFields

class Metadataflow(NameableArtefact):
    structure = models.ForeignKey(Reference, null=True, blank=True)
    translations = TranslatedFields()
