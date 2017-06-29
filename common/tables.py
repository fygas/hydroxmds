import django_tables2 as tables
from .models import Annotation 

class AnnotationTable(tables.Table):
    class Meta:
        model = Annotation 
