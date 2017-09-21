from collections import OrderedDict

from django.core import management
from django.core.management.base import BaseCommand 

from hydro_sdmx.models import (
    ConceptScheme, Concept, TextFormatInfo, Representation, Codelist, Code,
    Organisation,DataStructure, ObsValue, Dimension, Attribute
)

class Command(BaseCommand):
    help = 'Populate database'

    def create_organisations(self):
        orgs = ['HYDROSDMX', 'ESTAT', 'ECB']
        for org in orgs:
            Organisation.objects.update_or_create(id_code=org, name=org)
            self.stdout.write(self.style.SUCCESS('Succesfully created org %s"' % org))
        self.hydro = Organisation.objects.get(id_code='HYDROSDMX')

    def create_itemschemes(self):
        entries = {
            (ConceptScheme, Concept): OrderedDict((
                (('ALL_CONCEPTS', 'All concepts'), (
                    ('ORG_IDENTIFIER', 'Organisation identifier'),
                    ('ISNEWORGANISATION', 'New organisation flag'),
                    ('OBS_VALUE', 'Observation value'),
                    ('ORG_MEASURES', 'Organisation measures'),
                    ('VALID_FROM', 'Valid from'),
                    ('SOURCE', 'Source'),
                    ('CONF', 'Confidentiality'),
                )),
                (('ORG', 'Concept scheme for the measures of HYDRO_ORG DSD'), (
                    ('ORG_IDENTIFIER', 'Organisation identifier'),
                    ('BIRTH', 'Organisation birthdate'),
                    ('CLOSE', 'Organisation closedate'),
                )),
                (('ORG_INFO', 'Concept scheme for the measures of HYDRO_ORG_INFO DSD'), (
                    ('NAME', 'Name'),
                    ('ADDRESS', 'Address'),
                )),
            )), 
            (Codelist, Code): OrderedDict((
                (('CL_BOOLEAN', 'Boolean codelist'), (
                    ('TRUE', 'True'),
                    ('FALSE', 'False')
                )),
                (('CL_SOURCE', 'Boolean codelist'), (
                    ('STAT', 'STATISTICS'),
                    ('SUPER', 'SUPERVISION'),
                )),
                (('CL_CONF', 'Boolean codelist'), (
                    ('F', 'Free'),
                    ('C', 'Confidential'),
                ))
            ))
        }
        for (pm, cm), itemschemevalue in entries.items():
            for (pmidcode, pmname), value in itemschemevalue.items():
                wrapper, _ = pm.objects.update_or_create(id_code=pmidcode, name=pmname, agency=self.hydro)
                for idcode, name in value:
                    cm.objects.update_or_create(id_code=idcode, name=name, wrapper=wrapper)
                self.stdout.write(self.style.SUCCESS('Succesfully created(updated) itemscheme %s"' % pmname))

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
            self.stdout.write(self.style.SUCCESS('Succesfully created(updated) representation %s"' % idcode))

    def create_dsds(self):
        conceptwrapper = ConceptScheme.objects.get(id_code='ALL_CONCEPTS', agency=self.hydro)
        dsds = OrderedDict(( 
            (('HYDRO_ORG', 'Organisation management'), OrderedDict((
                ('dimensions', (
                    ('ISNEWORGANISATION', 'ISNEW', 'dimension', 'BOOLEAN', 1),
                    ('ORG_IDENTIFIER', 'IDCODE', 'dimension', 'STRING', 2),
                    ('ORG_MEASURES', 'MEASURE', 'measure', 'ORG', 3)
                )),
                ('obs_value',
                    ('OBS_VALUE', 'OBS_VALUE', 'STRING')
                )
            ))),
            (('HYDRO_ORG_INFO', 'Organisation information'), OrderedDict((
                ('dimensions', (
                    ('ORG_IDENTIFIER', 'IDCODE', 'dimension', 'STRING', 1),
                    ('VALID_FROM', 'START', 'dimension', 'DATETIME', 2),
                    ('ORG_MEASURES', 'MEASURE', 'measure', 'ORG_INFO', 3),
                )),
                ('obs_value',
                    ('OBS_VALUE', 'OBS_VALUE', 'STRING'),
                ),
                ('attributes', (
                    ('SOURCE', 'SOURCE', 'SOURCE', True),
                    ('CONF', 'CONF', 'CONF', True),
                ))
            )))
        ))

        for (dsdidcode, dsdname), dsddic in dsds.items(): 
            concept, idcode, representation = dsddic['obs_value']
            obs_value_kwargs = {
                'concept': Concept.objects.get(id_code=concept, wrapper=conceptwrapper),
                'representation': Representation.objects.get(id_code=representation)
            }
            obs_value, _ = ObsValue.objects.update_or_create(**obs_value_kwargs)

            dsdkwargs = {
                'id_code': dsdidcode,
                'name': dsdname,
                'agency': self.hydro,
                'obs_value': obs_value
            }
            wrapper, _ = DataStructure.objects.update_or_create(**dsdkwargs)

            for (concept, idcode, dimtype, representation, position) in dsddic['dimensions']:
                dimkwargs = {
                    'concept': Concept.objects.get(id_code=concept, wrapper=conceptwrapper),
                    'wrapper': wrapper,
                    'id_code': idcode,
                    'dimension_type': dimtype,
                    'position': position,
                    'is_concept_role': True,
                }
                if dimtype != 'measure':
                    dimkwargs['representation'] = Representation.objects.get(id_code=representation) 
                else:
                    dimkwargs['measure_representation'] = ConceptScheme.objects.get(id_code=representation, agency=self.hydro) 
                Dimension.objects.update_or_create(**dimkwargs)
            
            if dsddic.get('attributes'):
                for (concept, idcode, representation, required) in dsddic['attributes']:
                    attrkwargs = {
                        'concept': Concept.objects.get(id_code=concept, wrapper=conceptwrapper),
                        'wrapper': wrapper,
                        'id_code': idcode,
                        'is_concept_role': True,
                        'representation': Representation.objects.get(id_code=representation), 
                        'required': required,
                        'attached2measure': True
                    }
                    Attribute.objects.update_or_create(**attrkwargs)
            self.stdout.write(self.style.SUCCESS('Succesfully created(updated) dsd %s"' % dsdname))

    def handle(self, *args, **options):
        self.create_organisations()
        try:
            management.call_command('insertresource', 'ECB', 'codelist', 'CL_AREA')
            management.call_command('insertresource', 'ECB', 'conceptscheme', 'ECB_CONCEPTS')
        except ConnectionError:
            pass
        self.create_itemschemes()
        self.create_representations()
        self.create_dsds()
