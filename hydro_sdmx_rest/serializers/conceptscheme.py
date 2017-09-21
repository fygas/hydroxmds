from hydro_sdmx.models import (
    ConceptScheme, Concept
)

from ..constants import FIELDS
from .base import BaseModelSerializer

class ConceptSchemeSerializer(BaseModelSerializer):

    class Meta:
        model = ConceptScheme 
        fields = FIELDS['MAINTAINABLE'] + ('concepts',)  

class ConceptSerializer(BaseModelSerializer):

    class Meta:
        model = Concept 
        fields = FIELDS['ITEMWITHPARENT'] + ('representation', 'iso_concept_reference')
