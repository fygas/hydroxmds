from django.db import models

from ..settings import api_maxlen_settings
from ..utils.decorators import add_affairs

affairs = ['Organisation', 'Contact', 'OrganisationScheme', 'Codelist',
           'Code', 'Concept', 'ConceptScheme', 'DataStructure',
           'Dataflow', 'Group', 'Representation', 'Dimension',
           'Measure', 'Attribute', 'DataProvisionAgreement']

@add_affairs(affairs)
class Annotation(models.Model):
    id_code = models.CharField('ID', max_length=api_maxlen_settings.ID_CODE, blank=True)
    annotation_title = models.CharField('title', max_length=api_maxlen_settings.ANNOTATION_TITLE, blank=True)
    annotation_type = models.CharField('type', max_length=api_maxlen_settings.ANNOTATION_TYPE, blank=True)
    annotation_URL = models.URLField('URL', null=True, blank=True)
    annotation_text = models.TextField('annotation', blank=True)

    def __str__(self):
        return self.annotation_text 
