from .models import Organisation
from .tables import OrganisationTable
from .forms import OrganisationForm
from django_tables2 import SingleTableView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class OrganisationList(SingleTableView):
    model = Organisation
    table_class = OrganisationTable

class OrganisationCreate(CreateView):
    form_class = OrganisationForm
    model = Organisation

class OrganisationUpdate(UpdateView):
    form_class = OrganisationForm
    model = Organisation

class OrganisationDelete(DeleteView):
    model = Organisation
    success_url = reverse_lazy('hybrid:org_ids')
