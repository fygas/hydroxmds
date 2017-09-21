from django.db import models

from .abstract_postorg import MaintainableArtefact
from .data_structly import Dataflow
from .metadata_structly import Metadataflow
from .organisation import Organisation
from .organisation_scheme import DataProviderScheme

class DataProvisionAgreement(MaintainableArtefact):
    data_provider = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='data_provision_agreements')
    data_provider_scheme = models.ForeignKey(DataProviderScheme, on_delete=models.CASCADE, related_name='data_provision_agreements')
    structure_usage = models.ForeignKey(Dataflow, related_name='data_provider_agreements') 

class MetadataProvisionAgreement(MaintainableArtefact):
    data_provider = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='metadata_provision_agreements')
    data_provider_scheme = models.ForeignKey(DataProviderScheme, on_delete=models.CASCADE, related_name='metadata_provision_agreements')
    structure_usage = models.ForeignKey(Metadataflow, related_name='metadata_provider_agreements') 
