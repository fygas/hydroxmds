from django.db import models

from ..settings import api_maxlen_settings as maxlengths
from ..utils.decorators import add_affairs

affairs = ['Organisation', 'Contact', 'OrganisationScheme', 'Codelist', 'Code',
           'Concept', 'ConceptScheme', 'DataStructure', 'Dataflow',
           'Dimension', 'Attribute', 'ProvisionAgreement', 'AttachmentConstraint', 'ContentConstraint', 'Group', 'DimensionLevelAttribute', 'Observation', 'ObservationAttribute']

@add_affairs(affairs)
class Annotation(models.Model):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE, blank=True)
    annotation_title = models.CharField('title', max_length=maxlengths.ANNOTATION_TITLE, blank=True)
    annotation_type = models.CharField('type', max_length=maxlengths.ANNOTATION_TYPE, blank=True)
    annotation_URL = models.URLField('URL', null=True, blank=True)

    def __str__(self):
        return '%s:%s:%s' % (self.id_code, self.annotation_title, self.annotation_type)
