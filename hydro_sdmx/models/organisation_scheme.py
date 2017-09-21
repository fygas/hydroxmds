from django.db import models

from .abstract_postorg import MaintainableArtefact

class AgencyScheme(MaintainableArtefact):
    agencies = models.ManyToManyField('Organisation', related_name='agency_schemes')

class DataConsumerScheme(MaintainableArtefact):
    data_consumers = models.ManyToManyField('Organisation', related_name='data_consumer_schemes')

class DataProviderScheme(MaintainableArtefact):
    data_providers = models.ManyToManyField('Organisation', related_name='data_provider_schemes')

class OrganisationUnitScheme(MaintainableArtefact):
    organisation_units = models.ManyToManyField('Organisation', related_name='organisation_unit_schemes')
