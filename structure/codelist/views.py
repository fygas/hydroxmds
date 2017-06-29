from .models import Codelist
from .forms import CodelistForm 
from django.views.generic.edit import CreateView 


# Create your views here.
class CodelistCreate(CreateView):
    form_class = CodelistForm
    model = Codelist

