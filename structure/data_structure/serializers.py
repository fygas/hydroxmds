from .models import DataStructureComponentBase, DataStructureComponentGroup, DataStructureComponent, DataStructure
from common.serializers import BaseModelSerializer, AnnotationSerializer
from ..serializers import ConceptSerializer, RepresenationSerializer, ConceptSchemeSerializer
from rest_framework_recursive.fields import RecursiveField

class DataStructureComponentBaseSerializer(BaseModelSerializer):
    concept = ConceptSerializer() 

    class Meta:
        model = DataStructureComponentBase
        fields = ('class_name', 'id_code', 'concept', 'object_type')

class DataStructureComponentGroupSerializer(BaseModelSerializer):
    annotations = AnnotationSerializer(many=True)

    class Meta:
        model = DataStructureComponentGroup
        fields = ('class_name', 'id_code', 'group', 'annotations')

class DataStructureComponentSerializer(BaseModelSerializer):
    annotations = AnnotationSerializer(many=True)
    representation = RepresenationSerializer()
    measure_representation = ConceptSchemeSerializer()
    roles = ConceptSerializer(many=True)
    dims_attached = RecursiveField(many=True)
    base_component = DataStructureComponentBaseSerializer()
    group = DataStructureComponentGroupSerializer()
    groups = DataStructureComponentGroupSerializer(many=True)

    class Meta:
        model = DataStructureComponent
        fields = ('class_name', 'base_component', 'position', 'is_concept_role', 'representation', 'measure_representation', 'roles', 'dims_attached', 'primary_measure_attached', 'group', 'groups', 'annotations')

class DataStructureSerializer(BaseModelSerializer):
    components = DataStructureComponentSerializer(many=True)
    groups = DataStructureComponentGroupSerializer(many=True)
    dimension_annotations = AnnotationSerializer(many=True)
    measure_annotations = AnnotationSerializer(many=True)
    attribute_annotations = AnnotationSerializer(many=True)

    class Meta:
        model = DataStructure
        fields = ['class_name', 'id_code', 'components', 'groups', 'dimension_annotations', 'measure_annotations', 'attribute_annotations']
