from . import models
from . import serializers
from .parsers.sdmxml import SDMXMLParser
from rest_framework import viewsets
from django.core.files.base import ContentFile 

class SDMXMaintainableViewSet(viewsets.ModelViewSet):
    
    parser_classes = (SDMXMLParser,)

    def registration(self, request):
        filename = self.__class__.__name__+'.xml'
        sdmx_file = ContentFile(request.data)
        registration = models.Registration.objects.create(registrant=self.request.user)
        registration.sdmx_file.save(filename, sdmx_file)
        return registration

    def perform_create(self, request, serializer):
        registration = self.registration()
        serializer.save(registration=registration)
        
class CodelistViewSet(SDMXMaintainableViewSet):
    queryset = models.Codelist.objects.all()
    serializer_class = serializers.CodelistSerializer

    def perform_create(self, request):
        super().perform_create(request, serializers.CodelistSerializer)
