# from django.forms import ModelForm
# from extra_views import InlineFormSet
# from sdmx.forms import ArrayFieldSelectMultiple
from .models import OrganisationScheme
from structure.forms import ItemSchemeForm


# class ContactForm(ModelForm):
#     class Meta:
#         fields = []
#         widgets = {
#             'telephone': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
#             'fax': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
#             'uRI': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
#             'email': ArrayFieldSelectMultiple(attrs={'class': 'chosen'}),
#         }
#
#     class Media:
#         css = {
#             "all": ("chosen/chosen.min.css", )
#         }
#         js = ("js/jquery.min.js", "chosen/chosen.jquery.min.js")

class OrganisationSchemeForm(ItemSchemeForm):
    class Meta(ItemSchemeForm.Meta):
        model = OrganisationScheme 
