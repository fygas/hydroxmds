import inflection
from . import models
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .constants import ACTIONS

REFS = {
    'LOCAL': ['id'],
    'FULL': ['agencyid', 'id', 'version'],
}
FIELDS = {
    'KLASS': ('klass',) 
}
FIELDS['ANNOTATION'] = FIELDS['KLASS'] + ('id_code', 'annotation_title', 'annotation_type', 'annotation_URL', 'description_set')
FIELDS['IDENTIFIABLE'] = FIELDS['KLASS'] + ('id_code', 'uri', 'annotation_set')
FIELDS['NAMEABLE'] = FIELDS['IDENTIFIABLE'] + ('name_set', 'description_set')
FIELDS['VERSIONABLE'] = FIELDS['NAMEABLE'] + ('version', 'valid_from', 'valid_to')
FIELDS['MAINTAINABLE'] = FIELDS['VERSIONABLE'] + ('is_final', 'agency', 'registration')
FIELDS['ORGANISATIONSCHEME'] = FIELDS['MAINTAINABLE']
FIELDS['ITEM'] = FIELDS['NAMEABLE']
FIELDS['ITEMWITHPARENT'] = FIELDS['ITEM'] + ('parent',)
FIELDS['CODE'] = FIELDS['ITEMWITHPARENT']
FIELDS['CODELIST'] = FIELDS['MAINTAINABLE'] + ('code_set',)
FIELDS['REPRESENTATION'] = ('enumeration', 'text_type','is_sequence', 'interval', 'start_value', 'end_value', 'time_interval', 'start_time', 'end_time', 'min_length', 'max_length', 'min_value', 'max_value', 'pattern', 'is_multi_lingual')
FIELDS['CONCEPT'] = FIELDS['ITEMWITHPARENT'] + FIELDS['REPRESENTATION']
FIELDS['CONCEPTSCHEME'] = FIELDS['MAINTAINABLE'] + ('concept_set',)

    
class RegistrationSerializer(serializers.ModelSerializer):
    registrant = serializers.SlugRelatedField(
        slug_field = 'username',
        read_only = True,
    )
    sdmx_file_url = serializers.SerializerMethodField('get_sdmx_file_url') 
    
    def get_sdmx_file_url(self, object):
        return object.sdmx_file.url

    class Meta:
        model = models.Registration
        fields = ('creation_date', 'registrant', 'action', 'interactive', 'parent', 'sdmx_file_url', 'sdmx_location',)

class BaseModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        remove = kwargs.pop('exclude_fields', None)
        allowed = kwargs.pop('allowed_fields', None)
        super().__init__(*args, **kwargs)

        if remove is not None:
            not_allowed = set(remove)
            existing = set(self.fields.keys())
            for field_name in not_allowed - (not_allowed - existing):
                self.fields.pop(field_name)

        if allowed is not None:
            allowed = set(allowed)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    klass = serializers.SerializerMethodField()
    def get_klass(self, obj):
        return obj.__class__.__name__

class NameSerializer(BaseModelSerializer):
    class Meta:
        model = models.Name
        fields = ['lang', 'text']

class DescriptionSerializer(BaseModelSerializer):
    class Meta:
        model = models.Description
        fields = ['lang', 'text']

class AnnotationSerializer(BaseModelSerializer):
    description_set = DescriptionSerializer(many=True)
    class Meta:
        model = models.Annotation
        fields = FIELDS['ANNOTATION']

    def create(self, validated_data):
        description_set = validated_data.pop('description_set')
        annotation = models.Annotation.objects.create(**validated_data)
        for description in description_set:
            models.Description.objects.create(**description, annotation=annotation)
        return annotation

class IdentifiableSerializerMixin(serializers.Serializer):
    annotation_set = AnnotationSerializer(many=True, allow_null=True)

    class Meta:
        fields = FIELDS['IDENTIFIABLE']

    def create(self, validated_data, model):
        annotation_set = validated_data.pop('annotation_set')
        instance = model.objects.create(**validated_data)
        name = inflection.underscore(model.__name__)
        for annotation in annotation_set:
            annotation = AnnotationSerializer().create(**annotation)
            annotation.setattr(name, instance)
            annotation.save()
        return name, instance

class NameableSerializerMixin(IdentifiableSerializerMixin):
    name_set = NameSerializer(many=True) 
    description_set = DescriptionSerializer(many=True, allow_null=True) 
    class Meta:
        fields = FIELDS['NAMEABLE']

    def create(self, validated_data, model):
        name_set = validated_data.pop('name_set')
        description_set = validated_data.pop('description_set')
        name, instance = super().create(validated_data, model)
        for related_set,related_model in [(name_set, models.Name), (description_set, models.Description)]:
            for related in related_set:
                related = related_model(**related)
                related.setattr(name, instance)
                related.save()


class ItemSerializerMixin(NameableSerializerMixin):
    class Meta:
        fields = FIELDS['ITEM']

class ItemWithParentSerializerMixin(ItemSerializerMixin):
    parent = RecursiveField(allow_null=True) 
    class Meta:
        fields = FIELDS['ITEMWITHPARENT']

    def create(self, validated_data, model):
        parent = validated_data.pop('parent')
        if parent:
            parent = model.objects.get(**parent)
        instance = super().create(validated_data, model)
        instance.parent = parent
        instance.save()
        return instance

class OrganisationSerializer(ItemWithParentSerializerMixin, BaseModelSerializer):
    
    class Meta(ItemWithParentSerializerMixin.Meta):
        model = models.Organisation
        fields = FIELDS['ITEMWITHPARENT']

    def create(self, validated_data):
        super().create(validated_data, models.Organisation)

class MaintainableSerializerMixin(NameableSerializerMixin):
    agency = OrganisationSerializer(allowed_fields=['klass', 'id_code']) 
    action = serializers.ChoiceField(ACTIONS)
    registration = serializers.ReadOnlyField(source='registration.created_by.username')
    class Meta:
        fields = FIELDS['MAINTAINABLE']

    def create(self, validated_data, model):
        klass = validated_data.pop('klass').split('}')[1]
        if klass != self.__class__.__name__: return
        registration = validated_data.pop('registration')
        agency = validated_data.pop('agency')
        agency = models.Organisation.get(**agency) 
        instance = super().create(validated_data, model)
        instance.agency = agency
        instance.registration = registration
        instance.save()
        return instance


class OrganisationSchemeSerializer(MaintainableSerializerMixin, BaseModelSerializer):

    class Meta(MaintainableSerializerMixin.Meta):
        model = models.OrganisationScheme

    def create(self, validated_data):
        super().create(validated_data, models.OrganisationScheme)

class CodeSerializer(ItemWithParentSerializerMixin, BaseModelSerializer):

    class Meta(ItemWithParentSerializerMixin.Meta):
        model = models.Code

    def create(self, validated_data):
        super().create(validated_data, models.Code)

class CodelistSerializer(MaintainableSerializerMixin, BaseModelSerializer):

    code_set = CodeSerializer(many=True)

    class Meta:
        model = models.Codelist
        fields = FIELDS['CODELIST']

    def create(self, validated_data):
        code_set = validated_data.pop('code_set')
        instance = super().create(validated_data, models.Codelist)
        for code in code_set:
            code = CodeSerializer().create(**code)
            code.wrapper = instance
            code.save()

class ConceptSerializer(ItemWithParentSerializerMixin, BaseModelSerializer):
    iso_concept_reference = RecursiveField(allow_null=True) 
    class Meta:
        models = models.Concept
        fields = FIELDS['CONCEPT']

    def create(self, validated_data):
        iso = validated_data.pop('iso_concept_reference')
        enumeration = validated_data.pop('enumeration')
        instance = super().create(validated_data, models.Concept)
        if iso:
            iso = models.Concept.get(**iso)
            instance.iso_concept_reference = iso
        if enumeration:
            enumeration = models.codelist.get(**enumeration)
            instance.enumeration = enumeration
        instance.save()
        return instance

class ConceptSchemeSerializer(MaintainableSerializerMixin, BaseModelSerializer):

    concept_set = ConceptSerializer(many=True)

    class Meta(MaintainableSerializerMixin.Meta):
        models = models.ConceptScheme
        fields = FIELDS['CONCEPTSCHEME']

    def create(self, validated_data):
        concept_set = validated_data.pop('concept_set')
        instance = super().create(validated_data, models.ConceptScheme)
        for concept in concept_set:
            concept = ConceptSerializer().create(**concept)
            concept.wrapper = instance
            concept.save()
