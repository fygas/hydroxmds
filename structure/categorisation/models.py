from django.db import models
from hvad.models import TranslatedFields

from common.models import Reference
from ..models import MaintainableArtefact 

class Categorisation(MaintainableArtefact):
    Source = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Target = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    translations = TranslatedFields()
