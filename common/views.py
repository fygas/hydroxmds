from .models import Annotation 
from .tables import AnnotationTable
from .forms import AnnotationForm
from django_tables2 import SingleTableView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class AnnotationList(SingleTableView):
    model = Annotation
    table_class = AnnotationTable

class AnnotationCreate(CreateView):
    form_class = AnnotationForm
    model = Annotation

class AnnotationUpdate(UpdateView):
    form_class = AnnotationForm
    model = Annotation

class AnnotationDelete(DeleteView):
    model = Annotation
    success_url = reverse_lazy('hybrid:annotation-list')
