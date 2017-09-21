from hydro_sdmx.models import (
    TextFormatInfo, Representation, Code, Codelist
)

from ..constants import FIELDS
from .base import BaseModelSerializer

class CodelistSerializer(BaseModelSerializer):

    class Meta:
        model = Codelist
        fields = FIELDS['MAINTAINABLE'] + ('codes',)  

class CodeSerializer(BaseModelSerializer):

    class Meta:
        model = Code 
        fields = FIELDS['ITEMWITHPARENT']

class TextFormatInfoSerializer(BaseModelSerializer):

    class Meta:
        model = TextFormatInfo
        fields = FIELDS['TEXTFORMAT'] 

class RepresenationSerializer(BaseModelSerializer):

    class Meta:
        model = Representation 
        fields = FIELDS['REPRESENTATION'] 
