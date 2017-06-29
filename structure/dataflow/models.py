from django.db import models

from ..models import MaintainableArtefact 
from ..data_structure.models import DataStructure

#Dataflow Structure
class Dataflow(MaintainableArtefact):
    structure = models.ForeignKey(DataStructure, null=True, blank=True)
