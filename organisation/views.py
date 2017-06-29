from .models import Organisation
from .tables import OrganisationTable
from django_tables2 import SingleTableView

class OrganisationList(SingleTableView):
    model = Organisation
    table_class = OrganisationTable

