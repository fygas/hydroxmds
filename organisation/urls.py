from django.conf.urls import url
from .views import OrganisationSchemeCreate, get_organisation_scheme, ExampleView

app_name = 'structure:organisation'
urlpatterns = [
    url(r'^organisationscheme/add1/$', get_organisation_scheme, name='organisationScheme-add1'),
    url(r'^organisationscheme/add/$', OrganisationSchemeCreate.as_view(), name='organisationScheme-add'),
    url(r'^example/add/$', ExampleView.as_view(), name='example-add'),
]
