from django.conf.urls import url
from .views import SdmxMetaDataView

patterns = [
    r'^(?P<resource>\w+)/$',
    r'^(?P<resource>\w+)/(?P<agency>\w*)/$',   
    r'^(?P<resource>\w+)/(?P<agency>\w*)/(?P<resourceid>\w*)/$',   
    r'^(?P<resource>\w+)/(?P<agency>\w*)/(?P<resourceid>\w*)/(?P<version>\d\.\d)/$'
]
urlpatterns = [url(p, SdmxMetaDataView.as_view()) for p in patterns]
