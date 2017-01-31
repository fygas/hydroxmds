from django.db import models
from hvad.models import TranslatedFields

from ..models import MaintainableArtefact, ComponentList

#DataStructure Structure
class DataStructure(MaintainableArtefact):
    DataStructureComponents = models.ForeignKey('DataStructureComponents', null=True, blank=True, related_name='+')
    translations = TranslatedFields()

class DataStructureComponents(models.Model):
    DimensionList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Groups = models.ManyToManyField(ComponentList, related_name='+')
    AttributeList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    MeasuereList = models.ForeignKey(ComponentList, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
