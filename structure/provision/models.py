from django.db import models
from .structure_base import MaintainableArtefact
from hvad.models import TranslatedFields
from common.models import Reference

#Provision Structure
class Provision(MaintainableArtefact):
    StructureUsage = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    DataProvider = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
