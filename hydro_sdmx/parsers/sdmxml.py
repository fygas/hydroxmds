import collections
import inflection

from . import SDMXMLBaseParser

NS = {
    'message': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message',
    'structure':'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure',
    'common': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common',
}

ELEMENTINFO = {
    '{%s}Name' % NS['common']: {
    },
    '{%s}Description' % NS['common']: {
    },
    '{%s}Annotations' % NS['common']: {
        'skip2children': 'annotation_set',
    },
    '{%s}Annotation' % NS['common']: {
    },
    '{%s}Code' % NS['structure']: {
    },
    '{%s}Concept' % NS['structure']: {
    },
    '{%s}ConceptAgency' % NS['structure']: {
        'text_field': 'agency',
    },
    '{%s}ConceptSchemeID' % NS['structure']: {
        'text_field': 'maintainable_id',
    },
    '{%s}ConceptID' % NS['structure']: {
        'text_field': 'id_code',
    },
    '{%s}ISOConceptReference' % NS['structure']: {
        'store_as': 'concept',
    },
    '{%s}ConstraintAttachment' % NS['structure']: {
        'skip2children': True
    },
    '{%s}DataSet' % NS['structure']: {
        'store_as': 'datasets',
    },
    '{%s}SimpleDataSource' % NS['structure']: {
        'store_as': 'datasources',
    },
    '{%s}DataStructure' % NS['structure']: {
        'store_as': 'datastructures',
    },
    '{%s}DataFlow' % NS['structure']: {
        'store_as': 'dataflows',
    },
    '{%s}ProvisionAgreement' % NS['structure']: {
        'store_as': 'provisions',
    },
    '{%s}DataKeySet' % NS['structure']: {
        'store_as': 'data_key_sets',
    },
}

ATTR2FIELD = {
    'id': 'id_code',
    'agencyID': 'agency',
    'maintainableParentVersion': 'version',
    'maintainableParentID': 'maintainable_id',
}

def iterable(arg):
    return isinstance(arg, collections.Iterable) and not isinstance(arg, str)

def attr2field(attr):
    return ATTR2FIELD.get(attr, inflection.underscore(attr))

def item_class(wrapper_class):
    if wrapper_class == 'Codelist':
        return 'Code'
    if wrapper_class == 'ConceptScheme':
        return 'Concept'

class ElementInfo:
    def __init__(self, tag):
        self.tag = tag 
        self.clean_tag = tag.split('}')[1]
        self.underscore_tag = inflection.underscore(self.clean_tag)
        self.properties = ELEMENTINFO.get(tag, {})

    def get_klass_name(self):
        return self.properties.get('klass', self.clean_tag)
        
    def get_field_name(self, root_data):
        if not self.info.get('store_as') and not self.info.get('many'):
            return self.underscore_tag
        elif not self.properties.get('store_as'):
            return self.underscore_tag + '_set'
        else:
            if isinstance(self.properties['store_as'], str):
                return self.properties['store_as']
            try:
                root_class = root_data['tag']
                return self.properties['store_as'][root_class]
            except AttributeError:
                return self.properties['store_as'][None]

class SDMXMLParser(SDMXMLBaseParser):
    """
    SDMXMLParser
    """

    def _xml_convert(self, element):
        """
        convert the SDMX xml `element` into the corresponding python object
        """
        self.data = []
        self.header = self._parse_header(element)
        self.header_action = self._get_action_from_header()
        self.clean_tag = element.tag.split('}')[1].lower()
        getattr(self, '_parse_%s' % self.clean_tag.lower())(element)
        return self.data

    def _parse_header(self, element):
        return element[0]

    def _get_action_from_header(self):
        action = self.header.find('{%s}DataSetAction' % NS['message'])
        return action.text if action else 'Append'

    def _parse_structure(self, element):
        structures = element[1]
        for structure in structures:
            for inst in structure:
                self.inst = inst
                print(inst)
                data = self._parse_element(inst)
                print(data)
                self.data.append(self.transform(data))

    # def _parse_element(self, element):
    #     stack = [ self.gen_parse_element(element) ]
    #     result = None
    #     while stack:
    #         try:
    #             data, has_parent = stack[-1].send(result)
    #             stack.append(self.gen_parse_element(data, has_parent))
    #             result = None
    #         except StopIteration as exc:
    #             stack.pop()
    #             result = exc.value
    #     return result

    def _get_text_field(self, element, data):
        if element.text:
            text_field = self.elem_info.properties.get('text_field', 'text') 
            data[text_field] = element.text

    def _parse_element(self, element):
        self.elem_info = ElementInfo(element.tag)
        data = {
            attr2field(key): self._attr_type_convert(value)
            for key, value in element.items()
        }
        if element.tag not in ['URN', 'Ref']: data['tag'] = element.tag
        self._convert_agency(data)
        self._get_text_field(element, data)
        for child in element:
            child_elem_info = ElementInfo(child.tag)
            child_key = child_elem_info.get_field_name(data)
            child_data = self._parse_element(child) 
            if child_key in data:
                if isinstance(data[child_key], dict):
                    data[child_key] = [data[child_key]]
                data[child_key].append(child_data)
            else:
                data[child_key] = child_data
        data = self._final_conversion(data)
        return data

    def _final_conversion(self, data):
        #skip element and 
        self._skip2children(data)
        #fix isoelement if necessary
        self._fix_iso(data)
        #References
        self._reference_conversion(data)
        #Representation
        self._representation_conversion(data)
        self._class_conversion(data)
        #Fix constraints
        #a. fix klass to be either constraint or metaconstraint
        #b. fix dataset reference klass to be either dataflow or metadataflow
        self._fix_constraints(data)

    def _reference_conversion(self, data, elem_info):
        ref = data.get('ref')
        if ref:
            id_code = data.get('id_code')
            data = self._reference_ref_conversion(self, ref, id_code, data)
        else:
            urn = data.get('urn')
            if urn:
                data = self._reference_urn_conversion(self, urn)

    def _reference_ref_conversion(self, ref, id_code=None, data=None):
        if ref['maintainable_id']:
            ref['wrapper'] = self._create_wrapper(ref)
        ref['tag'] = self._get_ref_tag(ref, id_code, data) 
        if id_code: 
            ref['id_code'] = id_code
        self._convert_agency(ref)
        return ref

    def _get_ref_tag(self, ref, id_code, data):
        if ref['local']:
            if ref['package'] == 'codelist': return 'Code'
            elif ref['package'] == 'conceptscheme': return 'Concept'
        if id_code: 
            if 'DataSet' in data['tag']:
                return 'Dataflow'
            else:
                return 'Metadataflow'
        if ref['class'] == 'DataProvider': return 'Organsation' 
        return ref['class']


    def _reference_urn_conversion(self, urn):
        pass

    def _represenation_conversion(self, data):
        represenation = self.elem_info.properties.get('represenation')
        if not represenation: return
        if not data.get(represenation): return
        if data[represenation].get('text_format'):
            data.extend(data[represenation].pop('text_format'))
        if data[represenation].get('enumeration'):
            data['enumeration'] = data[represenation].pop('enumeration')


    def _create_wrapper(self, ref):
        if ref['version']:
            version = ref.pop('version')
        else: version = None
        return {
            'id_code': ref.pop('maintainable_id'), 
            'version': version or self._type_convert('1.0'),
            'agency': {'klass': 'Organisation', 'id_code': ref.pop('agency')}
        }

    def _class_conversion(self, data):
        tag = data['tag']
        if tag != self.elem_info.tag:
            data['klass'] = data.pop('tag')
        else:
            data['klass'] = self.elem_info.clean_tag 
            data.pop('tag')

    def _skip2children(self, data): 
        for key, value in data.items():
            elem_info = ElementInfo(value['tag'])
            field = elem_info.properties.get('skip2children')
            if field: data[field] = data.pop[key]

    # def _convert2many(self, data):
    #     for key, value in data.items():
    #         elem_info = ElementInfo(value['tag'])
    #         many = elem_info.properties.get('many')
    #         if many:
    #             if not iterable(value): data[key] = [value]

    def _fix_iso(self, data):
        if not 'ISOConceptReference' in data['tag']:
            return
        data['tag'] = 'Concept'
        data['wrapper'] = self._create_wrapper(data)

    def _fix_constraints(data):
        pass


    @staticmethod
    def _convert_agency(data):
        try:
            data['agency']
        except KeyError:
            pass
        else:
            data['agency'] = {'id_code': data['agency']}
