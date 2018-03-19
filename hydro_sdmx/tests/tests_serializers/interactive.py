from defusedxml.lxml import parse 
from lxml import etree

import os.path
from django.conf import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
schema_path = os.path.join(settings.BASE_DIR, 'sdmx', 'schemas', 'xml', 'SDMXMessage.xsd') 
schema_doc = parse(schema_path)
schema = etree.XMLSchema(schema_doc)
parser = etree.XMLParser(schema=schema, attribute_defaults=True) 

sdmx_path = os.path.join(settings.BASE_DIR, 'hydro_sdmx', 'tests', 'data', 'apro_dsd.xml') 

sdmx = parse(sdmx_path, parser)
