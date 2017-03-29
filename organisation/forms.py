from hvad.forms import TranslatableModelForm
from sdmx.forms import ArrayFieldSelectMultiple
from .models import OrganisationScheme


class ContactAdminForm(TranslatableModelForm):
    class Meta:
        fields = []
        widgets = {
            'telephone': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
            'fax': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
            'uRI': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
            'email': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
        }

    class Media:
        css = {
            "all": ("chosen/chosen.min.css", )
        }
        js = ("js/jquery.min.js", "chosen/chosen.jquery.min.js")

class OrganisationSchemeForm(TranslatableModelForm):
    class Meta:
        model = OrganisationScheme 
        fields = ['id_code', 'agencyID', 'name', 'description', 
                  'version', 'validFrom', 'validTo', 'uri']
