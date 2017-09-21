from . import constants
from hydro_sdmx.models import ConceptScheme, Codelist, DataStructure, Organisation
from .serializers.base import ConceptSchemeSerializer, CodelistSerializer
from .serializers.data_info import DataStructureSerializer 

import logging

from rest_framework.generics import ListAPIView 
from rest_framework.exceptions import APIException, NotFound 

logger = logging.getLogger('hydrosdmx.request')

meta_model_map = {
    'datastructure': (DataStructure, DataStructureSerializer),
    'codelist': (Codelist, CodelistSerializer),
    'conceptscheme': (ConceptScheme, ConceptSchemeSerializer),
}

class NotImplemented(APIException):
    status_code = 501
    default_detail = 'The requested resource is not implemented yet'
    default_code = 'Not implemented'

class SdmxMetaDataListMixin:
    allow_empty = False

    @staticmethod
    def validate_resource(resource):
        if resource not in constants.METARESOURCES:
            detail = '`resource` must be one of %s' % constants.METARESOURCES 
            raise NotFound(detail)
        if resource not in meta_model_map:
            raise NotImplemented('The requested resource `%s` is not yet implemented' % resource)

    @staticmethod
    def validate_agency(agency):
        try:
            agency_obj = Organisation.objects.get(id_code=agency)
        except Organisation.DoesNotExist:
            raise NotFound('%s is not a Maintainable agency' % agency)

    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        resource = self.kwargs['resource']
        self.validate_resource(resource)
        queryset = meta_model_map[resource][0].objects.all()
        agency = self.kwargs.get('agency')
        if agency: 
            self.validate_agency(agency)
            queryset = queryset.filter(agency=agency_obj)
        resourceid = self.kwargs.get('resourceid')
        if resourceid: queryset = queryset.filter(id_code=resourceid)
        version = self.kwargs.get('version')
        if version: queryset = queryset.filter(version=version)
        else: queryset = queryset.filter(version='1.0')
        # Check for references
        references = self.request.GET.get('references')
        if references:
        return queryset

    def get_serializer_class(self):
        return meta_model_map[self.kwargs['resource']][1]

class SdmxMetaDataView(SdmxMetaDataListMixin, ListAPIView):
    pass
