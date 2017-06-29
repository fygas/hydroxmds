
from .models import Organisation 
from common.serializers import BaseModelSerializer 

class OrganisationSerializer(BaseModelSerializer):
    class Meta:
        model = Organisation
        fields = ('class_name', 'id_code')