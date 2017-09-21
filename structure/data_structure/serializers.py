from .models import DataStructureConstraint, Group, Dimension, ObsValue, Attribute, DataStructure
from common.serializers import BaseModelSerializer

class DataStructureConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = DataStructureConstraint
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'attached2dsds', 'data_key_set', 'cube_region', 'annotations')

class GroupSerializer(BaseModelSerializer):

    class Meta:
        model = Group
        fields = ('class_name', 'id_code', 'attachment_constraint')

class DimensionSerializer(BaseModelSerializer):

    class Meta:
        model = Dimension
        fields = ('class_name', 'dsd', 'concept', 'id_code', 'position', 'is_concept_role', 'representation', 'roles', 'groups')

class ObsValueSerializer(BaseModelSerializer):

    class Meta:
        model = ObsValue 
        fields = ('class_name', 'dsd', 'concept', 'id_code', 'representation')

class AttributeSerializer(BaseModelSerializer):

    class Meta:
        model = Attribute
        fields = ('class_name', 'dsd', 'concept', 'id_code', 'is_concept_role', 'representation', 'roles','required', 'attached2dims', 'attached2measure', 'attached2dim_in_group', 'attached2groups')

class DataStructureSerializer:
    
    class Meta:
        model = DataStructure
        fields = ('class_name', 'id_code', 'name', 'description', 'agency', 'dimensions', 'obs_value', 'Attributes', 'groups', 'dimension_annotations', 'measure_annotations', 'attribute_annotations')
