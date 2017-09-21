from django.core.management.base import BaseCommand, CommandError
from pandasdmx import Request
from hydro_sdmx.models import (
    Organisation, Codelist, Code, ConceptScheme, Concept
)

class Command(BaseCommand):
    help = 'Get codelist using pandaSDMX and load it to database'

    resource2model ={
        'codelist': [Codelist, Code],
        'conceptscheme': [ConceptScheme, Concept]
    }

    def add_arguments(self, parser):
        parser.add_argument('agency', choices=('ECB', 'ESTAT'))
        parser.add_argument('resource', choices=('codelist', 'conceptscheme'))
        parser.add_argument('resource_id')
        
    def handle(self, *args, **options):
        resource = options['resource']
        Pm, Cm = self.resource2model[resource]
        agency = options['agency']
        rscid = options['resource_id']
        service = Request(agency)
        response = service.get(resource, rscid, agency)
        resource_sdmxob = getattr(response.msg, resource)[rscid]
        try:
            agency_djob = Organisation.objects.get(id_code=agency)
        except Organisation.DoesNotExist:
            raise CommandError('Organisation "%s" does not exist' % agency)
        wrapper, _ = Pm.objects.update_or_create(
            id_code=rscid,
            name=resource_sdmxob.name.get('en'),
            description = resource_sdmxob.description.get('en'),
            agency=agency_djob,
            is_final=resource_sdmxob.is_final,
        )

        for key, value in resource_sdmxob.items():
            try:
                description = value.description.get('en')
            except TypeError:
                description = None
            Cm.objects.update_or_create(
                id_code = key,
                wrapper = wrapper,
                name = value.name.get('en'),
                description = description,
            )
        self.stdout.write(self.style.SUCCESS('Succesfully loaded %s with id "%s"' % (resource, rscid)))
