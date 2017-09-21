from .base import BaseModelSerializer

from hydro_sdmx.models import ( 
    DataConstraint, Group, Dimension, ObsValue, Attribute, DataStructure,
    DataKeySet, DataKey, KeyValue, CubeRegion, KeyValueSet
)

class GroupSerializer(BaseModelSerializer):

    class Meta:
        model = Group
        fields = ('class_name', 'id_code', 'attachment_constraint')

class DimensionSerializer(BaseModelSerializer):

    class Meta:
        model = Dimension
        fields = ('class_name', 'dsd', 'concept', 'id_code', 'position', 'is_concept_role', 'representation', 'measure_representation', 'roles', 'groups')

class ObsValueSerializer(BaseModelSerializer):

    class Meta:
        model = ObsValue 
        fields = ('class_name', 'concept', 'representation')

class AttributeSerializer(BaseModelSerializer):

    class Meta:
        model = Attribute
        fields = ('class_name', 'dsd', 'concept', 'id_code', 'is_concept_role', 'representation', 'roles','required', 'attached2dims', 'attached2measure', 'attached2dim_in_group', 'attached2groups')

class DataConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = DataConstraint
        fields = ('class_name', 'id_code', 'agency', 'name', 'description', 'attached2dsds', 'attached2dataflows')

class DataKeySetSerializer(BaseModelSerializer):

    class Meta:
        model = DataKeySet
        fields = ('class_name', 'constraint', 'data_key_set_code')

class DataKeySerializer(BaseModelSerializer):

    class Meta:
        models = DataKey
        fields = ('class_name', 'data_key_set', 'data_key_code', 'is_included')

class KeyValueSerializer(BaseModelSerializer):
    
    class Meta:
        models = KeyValue
        fields = ('class_name', 'data_key', 'dimension', 'value')

class CubeRegionSerializer(BaseModelSerializer):

    class Meta:
        models = CubeRegion
        fields = ('class_name', 'constraint', 'cube_region_code', 'include')

class KeyValueSetSerializer(BaseModelSerializer):

    class Meta:
        model = KeyValueSet
        fields = ('class_name', 'cube_region', 'dimension', 'values', 'time_range')

class DataStructureSerializer(BaseModelSerializer):
    
    class Meta:
        model = DataStructure
        fields = ('class_name', 'id_code', 'name', 'description', 'agency', 'dimensions', 'obs_value', 'attributes', 'groups', 'dimension_annotations', 'measure_annotations', 'attribute_annotations')
