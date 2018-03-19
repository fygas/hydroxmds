import xml.etree.ElementTree as ET
from datetime import datetime
from functools import partial

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Codelist, Organisation, OrganisationScheme, Registration, Annotation, InternationalDescription, InternationalName, Code, ConceptScheme, Concept

NS = {'structure':'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure',
      'common': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common'}
    

attr_map = {
    None: (
        ('id_code', 'id'),
        ('uri', 'uri'),
        ('urn', 'urn'),
        ('version', 'version'),
        ('text_type', 'textType'),
    ),
    'date': (
        ('valid_from', 'validFrom'),
        ('valid_to', 'validTo'),
        ('urn', 'urn'),
    )
    'boolean': (

    )
        ('is_sequence', 'isSequence'),
        ('start_value', 'startValue'),
        ('end_value', 'endValue'),
        ('time_interval', 'timeInterval'),
        ('start_time', 'startTime'),
        ('end_time', 'endTime'),
    )
    
)
def add_not_transformed_attrs(cls):
    for 
    
class AttrConverter:

    def __init__(self, elem):
        self.elem = elem

    def not_transformed_attr(self, xml_attr):
        return self.elem.get(xml_attr)

    @property
    def is_final(self):
        if self.elem.get('isFinal') == 'true':
            return True

    def id_code(self):
        return self.elem.get('id')

    def uri(self):
        return self.elem.get('uri')

    def urn(self):
        return self.elem.get('urn')

    def version(self):
        return self.elem.get('version')

    def valid_from(self):
        value = self.elem.get('validFrom')

        if value: return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def valid_to(self):
        value = self.elem.get('validTo')

        if value: return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def agency(self):
        agency = self.elem.get('agencyID')

        if agency:
            return Organisation.objects.get(id_code=agency)

    def is_external_reference(self):
        if self.elem.get('isExternalReference')=='true':
            return True

class MetaSDMXHelper(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(name, bases, clsdict)
        try:
            clsobj.annot_field
        except AttributeError:
            clsobj.related_name = name.lower()
        return clsobj

class BaseSDMXHelper(metaclass=MetaSDMXHelper):
    
    attr_fields_map = []
    wrappers = []
    parent = False
    representation = False

    def __init__(self, elem):
        self.elem = elem
        self.converter = AttrConverter(elem)
        self.attr_fields = self.get_attr_fields()

    def get_attr_fields(self):
        return {
            attr_tuple[1]: getattr(self.converter, attr_tuple[1]) or self.fixed_attrs[attr_tuple[1]]

            for attr_tuple in self.attr_fields_map

            if attr_tuple[1]
        }

class IdentifiableHelper(BaseSDMXHelper):

    static_processes = ['annotations'] 
    attr_fields_map = BaseSDMXHelper.attr_fields_map + [
        ('id', 'id_code'),
        ('uri', 'uri'),
        ('urn', None),
    ]
    simple_element_fields_map = []

class NameableHelper(IdentifiableHelper):
    static_processes = IdentifiableHelper.static_processes + ['Name', 'Description'] 

class VersionableHelper(NameableHelper):
    attr_fields_map = NameableHelper.attr_fields_map + [
        ('version', 'version'),
        ('validFrom', 'valid_from'),
        ('validTo', 'valid_to'),
    ]

class MaintainableHelper(VersionableHelper):
    attr_info = VersionableHelper.attr_fields_map + [
        ('agencyID', 'agency'),
        ('isFinal', 'is_final'),
        ('isExternalReference', None),
    ]

class CodelistHelper(MaintainableHelper):
    wrappers = ['structure:Code']
    model = Codelist

class ItemHelper(NameableHelper):
    pass

class ItemWithParentHelper(ItemHelper):
    parent = True

class CodeHelper(ItemHelper):
    model = Code

class ConceptSchemeHelper(MaintainableHelper):
    wrappers = ['structure:Concept']
    model = ConceptScheme 

class ConceptHelper(ItemHelper):
    model = Concept 
    representation = 'structure:CoreRepresentation' 

class OrganisationSchemeHelper(MaintainableHelper):
    model = OrganisationScheme

class AgencySchemeHelper(OrganisationScheme):
    fixed_attrs = {'version': '1.0', 'is_final': False}

class DataConsumerSchemeHelper(OrganisationScheme):
    fixed_attrs = {'version': '1.0', 'is_final': False}

class DataProviderSchemeHelper(OrganisationScheme):
    fixed_attrs = {'version': '1.0', 'is_final': False}
    
class OrganisationUnitSchemeHelper(OrganisationScheme):
    pass

HELPERS = {
    'Codelist': CodelistHelper,
    'Code': CodeHelper,
    'AgencyScheme': AgencySchemeHelper,
    'DataConsumerScheme': DataConsumerSchemeHelper,
    'DataProviderScheme': DataProviderSchemeHelper,
    'OrganisationUnitScheme': OrganisationUnitSchemeHelper,
}

REFATTRS = ['agencyID', 'maintainableParentID', 'maintainableParentVersion', 'containerID', 'id', 'version', 'local', 'class', 'package']

@receiver(post_save, sender=Registration)
def upload(sender, **kwargs):
    """Test"""
    registration = kwargs['instance']

    if registration.interactive:
        return

    if registration.sdmx_file:
        sdmx_tree = ET.parse(registration.sdmx_file.path)
        sdmx_root = sdmx_tree.getroot()
    else:
        # TODO read from url
        pass
    SDMXMLParserAndSaver(sdmx_root, registration).parse_and_save()

class SDMXMLParserAndSaver:
    """Loads SDMX_ML trees to SDMX Django models"""
    def __init__(self, sdmxml_root, registration):
        """initializing"""
        self.root = sdmxml_root
        self.registration = registration 
        self.data_format = root.tag.split('}')[1]
        getattr(self, self.data_format)(root)

    def parse_and_save(self):
        data_format = self.root.tag.split('}')[1]
        getattr(self, 'parse_and_save_%s' % data_format)(self.root)

    def parse_and_save_structures(self, elem):
        structures = elem[1]
        for maintainable_wrapper in structures:
            for maintainable in maintainable_wrapper:
                artefact = maintainable.tag.split('}')[1]
                self.parse_and_save_generale(maintainable, artefact)

    def parse_and_save_generale(self, elem, artefact, base_helper=None):
        #create serializers and add there helper attributes instead of creating HELPER classes here
        #then create a method here to parse specific attributes of sdmxml elements
        helper = HELPERS[artefact](elem)
        kwargs = helper.attr_fields
        if not base_helper: 
            self.proceed(helper)
            kwargs['registration'] = self.registration
        kwargs['wrapper'] = base_helper.instance
        if helper.parent:
            parent_elem = elem.find('structure:Parent')
            if parent_elem: 
                parent = self.get_or_create_parent(elem)
                kwargs['parent'] = parent 
        if helper.representation:
            repr_elem = elem.find(helper.representation)
            if repr_elem:
                representation = self.get_representation(repr_elem)
                kwargs.extend(representation)
        instance = helper.model.objects.update_or_create(**kwargs)
        helper.instance = instance
        for process in helper.static_processes:
            getattr(self, 'process_%s' % process)(elem, helper, instance)
        if helper.wrappers:
            for wrapper in helper.wrappers:
                for subelem in elem.findall(wrapper):
                    artefact = wrapper.tag.split('}')[1]
                    self.process_specific(subelem, artefact, base_helper=helper)

    def get_representation(self, elem):
        text_format_elem = elem.find('structure:TextFormat')
        if text_format_elem:
        return 

        pass

    def get_or_create_parent(self, elem, model, base_helper):
        ref = self.get_ref(elem)
        try:
            return model.objects.get(id_code=ref['id'], wrapper=base_helper.instance)
        except model.DoesNotExist:
            related_elem = base_helper.elem.find('./structure:%s[@id=%s]' % (model, ref['id']))
            artefact = related_elem.tag.split('}')[1]
            self.process_specific(related_elem, artefact, base_helper)

    def get_ref(self, elem):
        ref_elem = elem.find('ref')
        if ref_elem:
            return {
                key: ref_elem.get(key)
                for key in REFATTRS
            }
        else:
            #parse URN
            pass

    def process_annotations(self, elem, helper, instance):
        for annotation in self.annotation_generator(elem):
            kwargs = {helper.related_name: instance,
                      'id_code': annotation['id_code']}
            kwargs.extend(annotation['simple_elements'])
            annotation_instance = Annotation.objects.create(**kwargs) 
            for annotation_text in annotation['annotation_texts']:
                InternationalDescription.objects.create(annotation=annotation_instance, **annotation_text)

    def process_inter_strings(self, elem, helper, instance, inter_model, related_name=None):
        if inter_model == InternationalName:
            elem_ns_name = 'common:name'
        else:
            elem_ns_name = 'common:description'
        related_name = related_name if related_name else helper.related_name
        for interdic in self.inter_string_generator(elem, elem_ns_name):
            kwargs = {related_name: instance}
            kwargs.extend(interdic)
            inter_model.objects.create(kwargs)

    process_inter_name = partial(process_inter_strings, inter_model=InternationalName)

    process_inter_description = partial(process_inter_strings, inter_model=InternationalDescription)

    def proceed(self, helper):
        stub = {
            key:value

            for key, value in helper.attr_fields

            if key in ['id_code', 'agency', 'version', 'isFinal']
        }
        existing = getattr(helper, 'model').objects.get(**stub)

        if not existing:
            return True

        if self.action != 'A' and not existing.isFinal:
            return True

    def annotation_generator(self, elem):
        elements_map = [
            ('common:AnnotationTitle', 'annotation_title'),
            ('common:AnnotationType', 'annotation_type'),
            ('common:AnnotationURL', 'annotation_URL'),
        ]
        for elem in self.elem.findall("./common:Annotations/common:Annotation", NS):
            id_code = elem.get('id')
            simple_elements = {
                elem_map[1]: elem.find(elem_map[0]).text 

                for elem_map in elements_map 
                if elem.find(elem_map[0])
            }
            yield {'id_code': id_code,
                   'simple_elements': simple_elements,
                   'annotation_texts': self.inter_string_generator(elem, 'common:name')}

    def inter_string_generator(self, elem, elem_ns_name):
        for elem in elem.findall(elem_ns_name, NS):
            lang = elem.get('lang', 'en')
            value = elem.text
            yield {
                'language':lang, 
                'value':value
            }
