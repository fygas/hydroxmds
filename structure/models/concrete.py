from .abstract import IdentifiableArtefact, NameableArtefact, Item, ItemScheme 

from django.urls import reverse
from common.constants import data_types 
from common.validators import re_validators 
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _
from structure.codelist.models import Codelist 


#Concrete models
class TextFormatInfo(NameableArtefact):
    annotations = None
    uri = None
    description = None
    text_type = models.CharField(max_length=settings.MAX_LENGTH, null=True, blank=True, choices=data_types)
    is_sequence = models.NullBooleanField(null=True, blank=True)
    interval = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    start_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    end_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    time_interval = models.DurationField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    min_length = models.PositiveIntegerField(null=True, blank=True)
    max_length = models.PositiveIntegerField(null=True, blank=True)
    min_value= models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    max_value = models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
    decimals = models.PositiveIntegerField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    is_multiLingual = models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return self.id_code

class Representation(IdentifiableArtefact):
    text_format = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    enumeration = models.ForeignKey(Codelist, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    enumeration_format = models.ForeignKey(TextFormatInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')

    def __str__(self):
        return '%s-%s-%s-%s' % (self.id_code, self.text_format, self.enumeration, self.enumeration_format)

class ConceptTag(Item):
    annotations = None
    description = None
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['IDType']], \
        unique=True
    )
    uri = None

class ConceptScheme(ItemScheme):
    id_code = models.CharField(
        'id', max_length=settings.MAX_LENGTH, \
        validators=[re_validators['NCNameIDType']], \
    )
    concepts = models.ManyToManyField(
        ConceptTag, 
        through='Concept', 
        through_fields=('concept_scheme', 'concept_tag'),
    )
    def get_absolute_url(self):
        return reverse('structure:concept:conceptscheme-index')

class Concept(NameableArtefact):
    id_code=None
    name=None
    concept_scheme = models.ForeignKey(ConceptScheme, on_delete=models.CASCADE)
    concept_tag = models.ForeignKey(ConceptTag, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    representation = models.ForeignKey(Representation, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    iso_concept_reference = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    uri = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = ('concept_scheme', 'concept_tag', 'representation')
    
    def clean(self):
        if self.parent:
            if self.concept_scheme!= self.parent.concept_scheme:
                raise ValidationError({
                    'parent': ValidationError(
                        _('''Parent and child concepts must be in the \
                            same ConceptScheme'''), code='local'
                    ),
                })

    #TODO set validations between representation and codelist

