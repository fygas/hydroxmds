from django.db import models

from .abstract import MaintainableArtefact

class DataProvisionAgreement(MaintainableArtefact):
    data_provider = models.ForeignKey('Organisation', on_delete=models.CASCADE, related_name='data_provision_agreements')
    data_provider_scheme = models.ForeignKey('OrganisationScheme', on_delete=models.CASCADE, related_name='data_provision_agreements')
    structure_usage = models.ForeignKey('Dataflow', related_name='data_provider_agreements') 
