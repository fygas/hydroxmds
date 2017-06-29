from django.conf.urls import url
from .views import OrganisationList

app_name = 'organisation'
urlpatterns = [
    url(r'^$', OrganisationList.as_view(), name='org_ids'),
]
