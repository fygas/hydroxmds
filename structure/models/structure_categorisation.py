from django.db import models
from common.mod import Reference
from .structure_base import MaintainableArtefact 
from hvad.models import TranslatedFields

class Categorisation(MaintainableArtefact):
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
