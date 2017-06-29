
from django.conf.urls import url
from .views import (
    AnnotationList, AnnotationCreate, AnnotationUpdate,
    AnnotationDelete
)

app_name = 'common'
urlpatterns = [
    url(r'annotation/$', AnnotationList.as_view(), name='annotation-list'),
    url(r'annotation/create$', AnnotationCreate.as_view(), name='annotation-create'),
    url(r'annotation/update/(?P<pk>[0-9]+)/$', AnnotationUpdate.as_view(), name='annotation-update'),
    url(r'annotation/delete/(?P<pk>[0-9]+)/$', AnnotationDelete.as_view(), name='annotation-delete'),
]
