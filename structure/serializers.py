from .models import TextFormatInfo, Representation, Concept, ConceptScheme
from common.serializers import BaseModelSerializer

class TextFormatInfoSerializer(BaseModelSerializer):
    class Meta:
        model = TextFormatInfo
        fields = ('class_name', 'id_code', 'text_type', 'is_sequence', 'interval', 'start_value', 'end_value', 'time_interval', 'start_time', 'end_time', 'min_length', 'max_length', 'min_value', 'max_value', 'decimals', 'pattern', 'is_multiLingual') 

class RepresenationSerializer(BaseModelSerializer):
    # text_format = TextFormatInfoSerializer()
    # enumeration = CodelistSerializer()
    # enumeration_format = TextFormatInfoSerializer()
    class Meta:
        model = Representation 
        fields = ('class_name', 'text_format', 'enumeration', 'enumeration_format') 

class ConceptSerializer(BaseModelSerializer):
    # annotations = AnnotationSerializer(many=True)
    # representation = RepresenationSerializer()

    class Meta:
        model = Concept
        fields = ('class_name', 'id_code', 'concept_scheme', 'name', 'description', 'representation', 'parent', 'iso_concept_reference', 'uri', 'annotations')

class ConceptSchemeSerializer(BaseModelSerializer):
    # annotations = AnnotationSerializer(many=True)
    # concepts = ConceptSerializer(many=True, remove=('concept_scheme')) 
    class Meta:
        model = ConceptScheme
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'concepts', 'annotations')
