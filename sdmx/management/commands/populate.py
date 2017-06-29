from django.core.management.base import BaseCommand 
from hybrid.models import Organisation
from structure.models import ( 
    ConceptScheme, ConceptTag, Concept, TextFormatInfo, Representation
)
from structure.data_structure.models import DataStructure, DataStructureComponent, DataStructureComponentBase
from structure.codelist.models import Code, Codelist
from collections import OrderedDict

class Command(BaseCommand):
    help = 'Populate database'

    def create_organisations(self):
        orgs = ['HYDROSDMX', 'ESTAT', 'ECB']
        for org in orgs:
            Organisation.objects.update_or_create(id_code=org)
        self.hydro = Organisation.objects.get(id_code='HYDROSDMX')

    def create_conceptschemes(self):
        ConceptScheme.objects.update_or_create(
            id_code='ALL_CONCEPTS',
            name='All concepts',
            agency=self.hydro
        )
        ConceptScheme.objects.update_or_create(
            id_code='ORG',
            name='Concept scheme for the measures of HYDRO_ORG DSD',
            agency=self.hydro,
        )
        ConceptScheme.objects.update_or_create(
            id_code='ORG_INFO',
            name='Concept scheme for the measures of HYDRO_ORG_INFO DSD',
            agency=self.hydro,
        )

    def create_concepts(self):
        new_entries = OrderedDict((
            ('ALL_CONCEPTS', (
                ('ORG_IDENTIFIER', 'Organisation identifier'),
                ('ISNEWORGANISATION', 'New organisation flag'),
                ('OBS_VALUE', 'Observation value'),
                ('ORG_MEASURES', 'Organisation measures'),
                ('VALID_FROM', 'Valid from'),
                ('SOURCE', 'Source'),
                ('CONF', 'Confidentiality'),
            )),
            ('ORG', (
                ('ORG_IDENTIFIER', 'Organisation identifier'),
                ('BIRTH', 'Organisation birthdate'),
                ('CLOSE', 'Organisation closedate'),
            )),
            ('ORG_INFO', (
                ('NAME', 'Name'),
                ('ADDRESS', 'Address'),
            )),
        )) 
        for key, value in new_entries.items():
            wrapper = ConceptScheme.objects.get(id_code=key)
            for idcode, name in value:
                entry, _ = ConceptTag.objects.update_or_create(
                    id_code=idcode,
                    name=name
                )
                Concept.objects.update_or_create(
                    concept_scheme = wrapper,
                    concept_tag = entry
                )

    def create_codelists(self):
        codelists = {
            ('CL_BOOLEAN', 'Boolean codelist'):(
                ('TRUE', 'True'),
                ('FALSE', 'False')
            ),
            ('CL_SOURCE', 'Boolean codelist'):(
                ('STAT', 'STATISTICS'),
                ('SUPER', 'SUPERVISION'),
            ),
            ('CL_CONF', 'Boolean codelist'):(
                ('F', 'Free'),
                ('C', 'Confidential'),
            ),
        }
        for (keycode, keyname), value in codelists.items():
            codelist, _ = Codelist.objects.update_or_create(id_code=keycode, name=keyname, agency=self.hydro)
            for idcode, name in value:
                Code.objects.update_or_create(id_code=idcode, name=name, codelist=codelist)

    def create_representations(self):
        entries = (
            ('DATETIME', 'DateTime'),
            ('STRING', 'String')
        )
        for idcode, texttype in entries:
            textformat, _ = TextFormatInfo.objects.update_or_create(
                id_code = idcode, 
                text_type = texttype
            )
            Representation.objects.update_or_create(
                id_code = idcode,
                text_format = textformat
            )
        entries = (
            ('BOOLEAN', 'CL_BOOLEAN'),
            ('SOURCE', 'CL_SOURCE'),
            ('CONF', 'CL_CONF'),
        )
        for idcode, enumeration in entries:
            Representation.objects.update_or_create(
                id_code=idcode,
                enumeration=Codelist.objects.get(id_code=enumeration, agency=self.hydro)
            )

    def create_dsds(self):
        DataStructure.objects.update_or_create(
            id_code='HYDRO_ORG', 
            name='Organisation management', 
            agency=self.hydro
        )
        DataStructure.objects.update_or_create(
            id_code='HYDRO_ORG_INFO', 
            name='Organisation information', 
            agency=self.hydro
        )
    

    def populate_dsds(self):
        conceptwrapper = ConceptScheme.objects.get(id_code='ALL_CONCEPTS', agency=self.hydro)
        dsds = OrderedDict(( 
            ('HYDRO_ORG', OrderedDict((
                ('dimensions', (
                    ('ISNEWORGANISATION', 'ISNEW', 'Dimension', 'BOOLEAN', 1),
                    ('ORG_IDENTIFIER', 'IDCODE', 'Dimension', 'STRING', 2),
                )),
                ('measure_dimension',
                    ('ORG_MEASURES', 'MEASURE', 'MeasureDimension', 'ORG', 3)
                ),
                ('obs_value',
                    ('OBS_VALUE', 'OBS_VALUE', 'PrimaryMeasure', 'STRING', 1)
                )
            ))),
            ('HYDRO_ORG_INFO', OrderedDict((
                ('dimensions', (
                    ('ORG_IDENTIFIER', 'IDCODE', 'Dimension', 'STRING', 1),
                    ('VALID_FROM', 'START', 'Dimension', 'DATETIME', 2),
                )),
                ('measure_dimension',
                    ('ORG_MEASURES', 'MEASURE', 'MeasureDimension', 'ORG_INFO', 3),
                ),
                ('obs_value',
                    ('OBS_VALUE', 'OBS_VALUE', 'PrimaryMeasure', 'STRING', 1),
                ),
                ('attributes', (
                    ('SOURCE', 'SOURCE', 'Attribute', 'SOURCE', True),
                    ('CONF', 'CONF', 'Attribute', 'CONF', True),
                ))
            )))
        ))

        for dsd, dsddic in dsds.items(): 
            orgdsd = DataStructure.objects.get(id_code=dsd, agency=self.hydro)
            components = set() 
            for dimset in dsddic['dimensions']:
                base_component, _ = DataStructureComponentBase.objects.update_or_create(
                    id_code=dimset[1],
                    concept=Concept.objects.get(concept_scheme=conceptwrapper, concept_tag=ConceptTag.objects.get(id_code=dimset[0])),
                    object_type=dimset[2],
                )
                component, _ = DataStructureComponent.objects.update_or_create(
                    base_component=base_component,
                    position=dimset[4],
                    representation = Representation.objects.get(id_code=dimset[3])
                )
                components.add(component)
            dimset = dsddic['measure_dimension']
            base_component, _ = DataStructureComponentBase.objects.update_or_create(
                id_code=dimset[1],
                concept=Concept.objects.get(concept_scheme=conceptwrapper, concept_tag=ConceptTag.objects.get(id_code=dimset[0])),
                object_type=dimset[2],
            )
            component, _ = DataStructureComponent.objects.update_or_create(
                base_component=base_component,
                position=dimset[4],
                measure_representation = ConceptScheme.objects.get(id_code=dimset[3], agency=self.hydro),
            )
            components.add(component)
            dimset = dsddic['obs_value']
            base_component, _ = DataStructureComponentBase.objects.update_or_create(
                id_code=dimset[1],
                concept=Concept.objects.get(concept_scheme=conceptwrapper, concept_tag=ConceptTag.objects.get(id_code=dimset[0])),
                object_type=dimset[2],
            )
            component, _ = DataStructureComponent.objects.update_or_create(
                base_component=base_component,
                position=dimset[4],
                representation = Representation.objects.get(id_code=dimset[3]),
            )
            components.add(component)
            for dimset in dsddic.get('attributes', []):
                base_component, _ = DataStructureComponentBase.objects.update_or_create(
                    id_code=dimset[1],
                    concept=Concept.objects.get(concept_scheme=conceptwrapper, concept_tag=ConceptTag.objects.get(id_code=dimset[0])),
                    object_type=dimset[2],
                )
                component, _ = DataStructureComponent.objects.update_or_create(
                    base_component=base_component,
                    representation = Representation.objects.get(id_code=dimset[3])
                )
                components.add(component)
            orgdsd.components.add(*components)

    def handle(self, *args, **options):
        self.create_organisations()
        # try:
        #     management.call_command('insertresource', 'ECB', 'codelist', 'CL_AREA')
        #     management.call_command('insertresource', 'ECB', 'conceptscheme', 'ECB_CONCEPTS')
        # except ConnectionError:
        #     pass
        self.create_conceptschemes()
        self.create_concepts()
        self.create_codelists()
        self.create_representations()
        self.create_dsds()
        self.populate_dsds()
