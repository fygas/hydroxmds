from extra_views import InlineFormSet
from django.forms import ModelForm
from .models import Code
class CodeForm(ModelForm):
    class Meta:
        model = Code
        fields = '__all__'

class CodeFormSet(InlineFormSet):
    model = Code
    form_class = CodeForm
