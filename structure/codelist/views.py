from extra_views import CreateWithInlinesView
from .models import Codelist
from .forms import CodeFormSet


# Create your views here.
class CodelistCreateView(CreateWithInlinesView):
    model = Codelist
    inlines = [CodeFormSet]
    fields = '__all__'
