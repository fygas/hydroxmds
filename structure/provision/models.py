from django.db import models
from hvad.models import TranslatedFields

from ..models import MaintainableArtefact
from common.models import Reference

#Provision Structure
class Provision(MaintainableArtefact):
    StructureUsage = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='structure_usages')
    DataProvider = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='data_providers')
    translations = TranslatedFields()
