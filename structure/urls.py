from django.conf.urls import include, url

app_name = 'structure'
urlpatterns = [
    url(r'codelist/', include('structure.codelist.urls')),
]
