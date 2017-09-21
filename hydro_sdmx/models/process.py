from django.db import models

from .abstract import AnnotableArtefact, NameableArtefact, IdentifiableArtefact
from .abstract_postorg import MaintainableArtefact
from .reference import ReferenceObject

from ..settings import api_maxlen_settings
from ..validators import re_validators

class Process(MaintainableArtefact):
    pass

class ProcessStep(NameableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
    )
    wrapper = models.ForeignKey(Process, verbose_name='Process', on_delete=models.CASCADE)
    inpout = models.ManyToManyField(ReferenceObject, related_name='process_step_inputs')
    output = models.ForeignKey(ReferenceObject, related_name='process_step_outputs')
    computation = models.ManyToManyField('Computation')
    transition = models.ManyToManyField('Transition')
    next_process = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Computation(AnnotableArtefact):
    description = models.TextField()
    local_id = models.CharField(
        max_length=api_maxlen_settings.ID_CODE, 
        validators=[re_validators['IDType']], 
        null=True, blank=True
    )
    software_package = models.CharField(max_length=api_maxlen_settings.NAME, null=True, blank=True)
    software_language= models.CharField(max_length=api_maxlen_settings.NAME, null=True, blank=True)
    software_version= models.CharField(max_length=api_maxlen_settings.VERSION, null=True, blank=True)

class Transition(IdentifiableArtefact):
    local_id = models.CharField(
        max_length=api_maxlen_settings.ID_CODE, 
        validators=[re_validators['IDType']], 
        null=True, blank=True
    )
    target_step = models.ForeignKey(ProcessStep, related_name='+')
    conditions = models.ManyToManyField('Condition')

class Condition(models.Model):
    condition = models.TextField()
