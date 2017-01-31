from django.db import models
from hvad.models import TranslatedFields

from common.constants import max_length

from ..models import MaintainableArtefact, NameableArtefact, IdentifiableArtefact
from common.models import AnnotableArtefact, Text, Reference

#Process Structure
class Process(MaintainableArtefact):
    ProcessSteps = models.ManyToManyField('ProcessStep', related_name='+')
    translations = TranslatedFields()

class ProcessStep(NameableArtefact):
    Input = models.ManyToManyField('InputOutpout', related_name='+')
    Outpout = models.ManyToManyField('InputOutpout', related_name='+')
    Computation = models.ForeignKey('Computation', on_delete=models.CASCADE, related_name='+')
    Transitions = models.ManyToManyField('Transition', related_name='+') 
    ProcessSteps = models.ManyToManyField('self')
    translations = TranslatedFields()

class Transition(IdentifiableArtefact):
    TargetStep = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    Conditions = models.ManyToManyField(Text, related_name='+')
    localID  = models.CharField(max_length=max_length['id'], null=True, blank=True)
    translations = TranslatedFields()

class Computation(AnnotableArtefact):
    localID  = models.CharField(max_length=max_length['id'], null=True, blank=True)
    softwarePackage = models.CharField(max_length=max_length['id'], null=True, blank=True)
    softwareLanguage = models.CharField(max_length=max_length['id'], null=True, blank=True)
    softwareVersion = models.CharField(max_length=max_length['id'], null=True, blank=True)
    tranaslations = TranslatedFields(
        Description = models.TextField(null=True, blank=True)
    )

class InputOutpout(AnnotableArtefact):
    localID  = models.CharField(max_length=max_length['id'], null=True, blank=True)
    ObjectType = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()
