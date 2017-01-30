from django.db import models
from .structure_base import MaintainableArtefact, NameableArtefact, IdentifiableArtefact
from common.models import AnnotableArtefact, Text, Reference
from hvad.models import TranslatedFields
from . import enum

#Process Structure
class Process(MaintainableArtefact):
    ProcessSteps = models.ManyToManyField('ProcessStep', on_delete=models.CASCADE, null=True, blank=True)
    translations = TranslatedFields()

class ProcessStep(NameableArtefact):
    Input = models.ManyToManyField('InputOutpout', on_delete=models.CASCADE, null=True, blank=True)
    Outpout = models.ManyToManyField('InputOutpout', on_delete=models.CASCADE, null=True, blank=True)
    Computation = models.ForeignKey('Computation', on_delete=models.CASCADE, null=True, blank=True)
    Transitions = models.ManyToManyField('Transition', on_delete=models.CASCADE, null=True, blank=True)
    ProcessSteps = models.ManyToManyField('self', on_delete=models.CASCADE, null=True, blank=True)

class Transition(IdentifiableArtefact):
    TargetStep = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    Conditions = models.ManyToManyField(Text, on_delete=models.CASCADE, null=True, blank=True)
    localID  = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)

class Computation(AnnotableArtefact):
    localID  = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    softwarePackage = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    softwareLanguage = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    softwareVersion = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    tranaslations = TranslatedFields(
        Description = models.TextField(null=True, blank=True)
    )

class InputOutpout(AnnotableArtefact):
    localID  = models.CharField(max_length=enum.max_length['id'], null=True, blank=True)
    ObjectType = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
