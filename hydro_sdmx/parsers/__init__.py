from datetime import datetime
from datetime import timedelta 
from decimal import Decimal
import isodate

from defusedxml.lxml import parse 
from lxml import etree

from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser
from django.utils import six

from ..settings import api_settings

SCHEMADOC = parse(api_settings.SDMXMLSCHEMA)
SCHEMA = etree.XMLSchema(SCHEMADOC)

ATTR2TYPE = {
    'validFrom': datetime,
    'validTo': datetime,
    'isFinal': bool,
    'isSequence': bool,
    'interval': Decimal,
    'startValue': Decimal,
    'endValue': Decimal,
    'timeInterval': timedelta,
    'startTime': datetime,
    'endTime': datetime,
    'minLength': int,
    'maxLength': int,
    'minValue': Decimal,
    'maxValue': Decimal,
    'decimals': int,
    'isMultiLingual': bool,
    'cascade': bool,
    'startInclusive': bool,
    'endInclusive': bool,
    'isIncluded': bool,
}

class SDMXMLBaseParser(BaseParser):
    """
    SDMXMLBaseParser
    """

    media_type = 'application/xml'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as XML and returns the resulting data.
        """

        parser_context = parser_context or {}
        parser = etree.XMLParser(schema=SCHEMA, attribute_defaults=True, remove_blank_text=True, remove_comments=True, ns_clean=True)
        try:
            tree = parse(stream, parser=parser, forbid_dtd=True)
        except (etree.ParseError, ValueError) as exc:
            raise ParseError('XML parse error - %s' % six.text_type(exc))
        data = self._xml_convert(tree.getroot())

        return data

    def _attr_type_convert(self, attr, value):
        """
        Converts the attribute value returned by the XMl parser into the equivalent
        Python type
        """
        #if not in ATTR2TYPE return string
        if attr not in ATTR2TYPE:
            return value

        getattr(self, '_%s_type_convert' % ATTR2TYPE[attr].lower())(value)

    def _datetime_type_convert(value):
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def _int_type_convert(value):
        return int(value)

    def _decimal_type_convert(value):
        return Decimal(value)

    def _timedelta_type_convert(value):
        return isodate.parse_duration(value)
