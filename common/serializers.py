from rest_framework import serializers
from .models import Annotation

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
