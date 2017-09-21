
from common.serializers import BaseModelSerializer 
from .models import Codelist, Code 

    
class CodeSerializer(BaseModelSerializer):
    # annotations = AnnotationSerializer(many=True)
    # parent = RecursiveField(allow_null=True)

    class Meta:
        model = Code 
        fields = ('class_name', 'id_code', 'name', 'description', 'parent', 'annotations')
    
class CodelistSerializer(BaseModelSerializer):
    # annotations = AnnotationSerializer(many=True)
    # codes = CodeSerializer(many=True)
    # agency = OrganisationSerializer()

    class Meta:
        model = Codelist
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'codes', 'annotations')
