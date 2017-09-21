from .models import TextFormatInfo, Representation, Concept, ConceptScheme, Annotation, Code, Codelist
from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        remove = kwargs.pop('remove', None)
        super(BaseModelSerializer, self).__init__(*args, **kwargs)

        if remove is not None:
            not_allowed = set(remove)
            existing = set(self.fields.keys())
            for field_name in not_allowed - (not_allowed - existing):
                self.fields.pop(field_name)

    class_name = serializers.SerializerMethodField()
    def get_class_name(self, obj):
        return obj.__class__.__name__

class AnnotationSerializer(BaseModelSerializer):

    class Meta:
        model = Annotation
        fields = ('class_name', 'annotation_title', 'annotation_type', 'annotation_URL', 'annotation_text', 'id_code')

class CodelistSerializer(BaseModelSerializer):

    class Meta:
        model = Codelist
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'annotations')

class CodeSerializer(BaseModelSerializer):

    class Meta:
        model = Code 
        fields = ('class_name', 'id_code', 'wrapper', 'name', 'description', 'parent', 'annotations')
    

class TextFormatInfoSerializer(BaseModelSerializer):

    class Meta:
        model = TextFormatInfo
        fields = ('class_name', 'id_code', 'text_type', 'is_sequence', 'interval', 'start_value', 'end_value', 'time_interval', 'start_time', 'end_time', 'min_length', 'max_length', 'min_value', 'max_value', 'decimals', 'pattern', 'is_multiLingual') 

class RepresenationSerializer(BaseModelSerializer):

    class Meta:
        model = Representation 
        fields = ('class_name', 'text_format', 'enumeration', 'enumeration_format') 

class ConceptSchemeSerializer(BaseModelSerializer):

    class Meta:
        model = ConceptScheme
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'annotations')

class ConceptSerializer(BaseModelSerializer):

    class Meta:
        model = Concept
        fields = ('class_name', 'id_code', 'wrapper', 'name', 'description', 'representation', 'parent', 'iso_concept_reference', 'uri', 'annotations')

