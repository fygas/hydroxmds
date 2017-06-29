from django import forms

agencies = (
    ('ABS', 'Australian Bureau of Statistics'),
    ('ECB', 'European Central Bank'),
    ('ESTAT', 'Eurostat'),
    ('INSEE', 'French National Institute for Statistics'),
    ('IMF', 'International Monetary Fund'),
    ('OECD', 'Organisation for Economic Cooperation and Development'),
    ('UNSD', 'United Nations Statistics Division'),
    ('UNESCO', 'UNESCO'),
)

resources = [
    'dataflow', 'datastructure', 'data', 'categoryscheme', 'codelist',
    'conceptscheme',
]

class BaseSdmxForm(forms.Form):
    agency = forms.ChoiceField(agencies)
    resource = forms.ChoiceField(resources)
