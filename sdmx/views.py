from . import constants
from base.models import ConceptScheme, Codelist
from data_info.models import DataStructure 
from base.serializers import ConceptSchemeSerializer, CodelistSerializer
from data_info.serializers import DataStructureSerializer 

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

    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        resource = self.args[0]
        if resource not in constants.METARESOURCES:
            detail = '`resource` must be one of %s' % constants.METARESOURCES 
            raise NotFound(detail)
        if resource not in meta_model_map:
            raise NotImplemented('The requested resource `%s` is not yet implemented' % resource)
        queryset = meta_model_map[resource][0].objects.all()
        agency = self.kwargs.get('agency')
        if agency: queryset = queryset.filter(agency=agency)
        resourceid = self.kwargs.get('resourceid')
        if resourceid: queryset = queryset.filter(id_code=resourceid)
        version = self.kwargs.get('version')
        if version: queryset = queryset.filter(version=version)
        else: queryset = queryset.filter(version='1.0')
        return queryset

    def get_serializer_class(self):
        return meta_model_map[self.args[0]][1]

class SdmxMetaDataView(SdmxMetaDataListMixin, ListAPIView):
    pass
