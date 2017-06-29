import django_tables2 as tables
from .models import Organisation

class OrganisationTable(tables.Table):
    foo = tables.CheckBoxColumn(empty_values=())

    class Meta:
        model = Organisation
