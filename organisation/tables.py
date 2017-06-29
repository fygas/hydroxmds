import django_tables2 as tables
from .models import Organisation

class OrganisationTable(tables.Table):
    class Meta:
        model = Organisation
