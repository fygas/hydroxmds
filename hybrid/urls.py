from django.conf.urls import url
from .views import (
    OrganisationList, OrganisationCreate, OrganisationUpdate,
    OrganisationDelete
)

app_name = 'hybrid'
urlpatterns = [
    url(r'organisation/$', OrganisationList.as_view(), name='org-list'),
    url(r'organisation/create$', OrganisationCreate.as_view(), name='org-create'),
    url(r'organisation/update/(?P<pk>[0-9]+)/$', OrganisationUpdate.as_view(), name='org-update'),
    url(r'organisation/delete/(?P<pk>[0-9]+)/$', OrganisationDelete.as_view(), name='org-delete'),
]
