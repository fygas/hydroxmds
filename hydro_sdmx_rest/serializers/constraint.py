
from hydro_sdmx.models import (
    AttachmentConstraint, ContentConstraint, DataKeySet, DataKey, KeyValue,
    CubeRegion, KeyValueSet, MetaattachmentConstraint, MetacontentConstraint,
    MetadataKeySet, MetadataKey, SimpleDataKey, SimpleDimValue, MetakeyValue,
    MetadataTargetRegion, MetakeyValueSet, TimeValue, MetaattrValueSet
)

from ..constants import FIELDS
from .base import BaseModelSerializer

class AttachmentConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = AttachmentConstraint 
        fields = FIELDS['ATTACHMENTCONSTRAINT'] + ('data_key_sets',)

class ContentConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = ContentConstraint 
        fields = FIELDS['CONTENTCONSTRAINT'] + ('data_key_sets',)

class DataKeySetSerializer(BaseModelSerializer):

    class Meta:
        model = DataKeySet 
        fields = FIELDS['DATAKEYSET'] + ('data_keys',)

class DataKeySerializer(BaseModelSerializer):

    class Meta:
        model = DataKey 
        fields = FIELDS['DATAKEY'] + ('key_values',)

class KeyValueSerializer(BaseModelSerializer):

    class Meta:
        model = KeyValue 
        fields = FIELDS['KEYVALUE']

class CubeRegionSerializer(BaseModelSerializer):

    class Meta:
        model = CubeRegion
        fields = FIELDS['CUBEREGION'] + ('data_keys',)

class KeyValueSetSerializer(BaseModelSerializer):

    class Meta:
        model = KeyValueSet
        fields = FIELDS['KEYVALUESET']

class MetaattachmentConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = MetaattachmentConstraint
        fields = FIELDS['METAATTACHMENTCONSTRAINT'] + ('metadata_key_sets',)

class MetacontentConstraintSerializer(BaseModelSerializer):

    class Meta:
        model = MetacontentConstraint
        fields = FIELDS['METACONTENTCONSTRAINT'] + ('metadata_key_sets', 'metadata_target_regions')

class MetadataKeySetSerializer(BaseModelSerializer):

    class Meta:
        model = MetadataKeySet 
        fields = FIELDS['METADATAKEYSET'] + ('metadata_keys',)

class MetadataKeySerializer(BaseModelSerializer):

    class Meta:
        model = MetadataKey 
        fields = FIELDS['METADATAKEY'] + ('metakey_values',)

class MetakeyValueSerializer(BaseModelSerializer):

    class Meta:
        model = MetakeyValue
        fields = FIELDS['METAKEYVALUE']

class SimpleDataKeySerializer(BaseModelSerializer):
    class Meta:
        model = SimpleDataKey
        fields = FIELDS['SIMPLEDATAKEY'] + ('simple_dim_values',)
                
class SimpleDimValueSerializer(BaseModelSerializer):
    class Meta:
        model = SimpleDimValue
        fields = FIELDS['SIMPLEDIMVALUE']

class MetadataTargetRegion(BaseModelSerializer):

    class Meta:
        model = MetadataTargetRegion
        fields = FIELDS['METADATATARGETREGION'] + ('metakey_value_sets', 'metaattr_value_sets')

class MetakeyValueSetSerializer(BaseModelSerializer):

    class Meta:
        model = MetakeyValueSet 
        fields = FIELDS['METAKEYVALUESET']

class TimeValueSerializer(BaseModelSerializer):

    class Meta:
        model = TimeValue
        fields = FIELDS['TIMEVALUE']

class MetaattrValueSetSerializer(BaseModelSerializer):

    class Meta:
        model = MetaattrValueSet
        fields = FIELDS['METAATTRVALUESET']
