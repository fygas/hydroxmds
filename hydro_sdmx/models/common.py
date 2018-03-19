from django.db import models

from ..settings import api_maxlen_settings as maxlengths
from ..utils.decorators import add_affairs

name_affairs = [
    'Organisation', 'OrganisationScheme', 'Codelist', 'Code', 'Concept',
    'ConceptScheme', 'DataStructure', 'Dataflow', 'ProvisionAgreement',
    'AttachmentConstraint', 'ContentConstraint'
]
complex_name_affairs = [
    ('Contact', 'names', 'contact_name'),
    ('Contact', 'roles', 'contact_role'),
    ('Contact', 'departments', 'contact_department'),
]

LANGUAGES = (
    ('en', 'English'),
    ('gr', 'Greek'),
    ('fr', 'French'),
)

@add_affairs(name_affairs+complex_name_affairs)
class Name(models.Model):
    lang = models.CharField(max_length=maxlengths.LANG, default='en', choices=LANGUAGES)
    text = models.CharField(max_length=maxlengths.NAME)

description_affairs = name_affairs + [('Annotation', 'annotation_texts', 'annotation')]

@add_affairs(description_affairs)
class Description(models.Model):
    lang = models.CharField(max_length=maxlengths.LANG, default='en', choices=LANGUAGES)
    text = models.TextField()
