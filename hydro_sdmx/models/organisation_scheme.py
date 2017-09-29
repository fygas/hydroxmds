from django.db import models

from .abstract_postorg import MaintainableArtefact

class AgencyScheme(MaintainableArtefact):
    items = models.ManyToManyField('Organisation', verbose_name='agencies', related_name='agency_schemes')

class DataConsumerScheme(MaintainableArtefact):
    items = models.ManyToManyField('Organisation', verbose_name='data consumers', related_name='data_consumer_schemes')

class DataProviderScheme(MaintainableArtefact):
    items = models.ManyToManyField('Organisation', verbose_name='data providers', related_name='data_provider_schemes')

class OrganisationUnitScheme(MaintainableArtefact):
    items = models.ManyToManyField('Organisation', verbose_name='Organisation units', related_name='organisation_unit_schemes')
