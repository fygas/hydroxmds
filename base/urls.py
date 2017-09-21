
from django.conf.urls import url
from sdmx.views import BaseSdmxMetaDataView

patterns = [
    r'^$',
    r'^(?P<agency>\w+)/$',   
    r'^(?P<agency>\w+)//$',   
    r'^(?P<agency>\w+)/(?P<resourceid>\w+)/$',   
    r'^(?P<agency>\w+)/(?P<resourceid>\w+)/(?P<version>\w+)/$'
]
urlpatterns = [url(p, BaseSdmxMetaDataView.as_view()) for p in patterns]
