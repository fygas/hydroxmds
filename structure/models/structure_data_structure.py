from django.db import models
from .structure_base import MaintainableArtefact, ComponentList
from hvad.models import TranslatedFields

#DataStructure Structure
class DataStructure(MaintainableArtefact):
    DataStructureComponents = models.ForeignKey('DataStructureComponents', null=True, blank=True)
    translations = TranslatedFields()

class DataStructureComponents(models.Model):
    DimensionList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True)
    Groups = models.ManyToManyField(ComponentList, on_delete=models.CASCADE, null=True, blank=True)
    AttributeList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True)
    MeasuereList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True)

