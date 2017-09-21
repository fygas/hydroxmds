from .base import BaseModelSerializer 

from hydro_sdmx.models import Organisation 

class OrganisationSerializer(BaseModelSerializer):
    class Meta:
        model = Organisation
        fields = ('class_name', 'id_code')
