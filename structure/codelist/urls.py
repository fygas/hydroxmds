from django.conf.urls import url
from .views import CodelistCreate


app_name = 'codelist'
urlpatterns = [
    url(r'create$', CodelistCreate.as_view(), name='codelist-create')
]
