
from hydro_sdmx.models import (
    DataPartialDimKey, PartialDimValue
)

from ..constants import FIELDS
from .base import BaseModelSerializer

class DataPartialDimKeySerializer(BaseModelSerializer):

    class Meta:
        model = DataPartialDimKey 
        fields = FIELDS['DATAPARTIALDIMKEY']

class DataPartialDimValueSerializer(BaseModelSerializer):

    class Meta:
        model = DataPartialDimKey 
        fields = FIELDS['DATAPARTIALDIMKEY']

