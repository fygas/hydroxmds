from hydro_sdmx.models import (
    CategoryScheme, Category, Categorization, ReportingTaxonomy, ReportingCategory 
)

from ..constants import FIELDS
from .base import BaseModelSerializer

class CategorySchemeSerializer(BaseModelSerializer):

    class Meta:
        model = CategoryScheme 
        fields = FIELDS['MAINTAINABLE'] + ('categories',)  

class CategorySerializer(BaseModelSerializer):

    class Meta:
        model = Category
        fields = FIELDS['ITEMWITHPARENT']

class CategorizationSerializer(BaseModelSerializer):

    class Meta:
        model = Categorization
        fielsd = FIELDS['CATEGORIZATION']

class ReportingTaxonomySerializer(BaseModelSerializer):
    class Meta:
        model = ReportingTaxonomy 
        fields = FIELDS['MAINTAINABLE'] + ('categories',)

class ReportingCategorySerializer(BaseModelSerializer):

    class Meta:
        model = ReportingCategory 
        fields = FIELDS['ITEMWITHPARENT']
