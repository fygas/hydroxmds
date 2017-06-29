from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout 
from .models import Organisation 

class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = ['id_code', 'annotations']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        

class ItemSchemeForm(ModelForm):
    class Meta:
        fields = ['id_code', 'agencyID', 'name', 'description', 
                  'version', 'validFrom', 'validTo', 'uri', 
                  'annotations']

    def __init__(self, *args, **kwargs):
        super(ItemSchemeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            *self.Meta.fields, 
            Submit('sumbit', 'Submit')
        )

class ItemForm(ModelForm):
    class Meta:
        fields = ['id_code', 'name', 'description', 
                  'uri', 'parent', 'annotations']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            *self.Meta.fields, 
            Submit('sumbit', 'Submit')
        )

# class OrganisationForm(ItemForm):
#     class Meta(ItemForm.Meta):
#         model = Organisation 
