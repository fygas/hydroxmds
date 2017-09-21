from hydro_sdmx.models import Annotation

from .base import BaseModelSerializer
from ..constants import FIELDS

class AnnotationSerializer(BaseModelSerializer):

    class Meta:
        model = Annotation
        fields = FIELDS['TRACKING'] + FIELDS['ANNOTATION'] 
