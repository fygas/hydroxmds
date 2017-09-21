from django.db import models

from .abstract import ItemWithParent, Item
from .abstract_postorg import MaintainableArtefact
from .data_structly import DataStructure, Dataflow
from .metadata_structly import MetadataStructure, Metadataflow
from .reference import ReferenceObject

from ..settings import api_maxlen_settings
from ..validators import re_validators

class CategoryScheme(MaintainableArtefact):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['NCNameIDType']],
    )

class Category(ItemWithParent):
    id_code = models.CharField(
        'id', max_length=api_maxlen_settings.ID_CODE,
        validators=[re_validators['IDType']],
    )
    wrapper = models.ForeignKey(CategoryScheme, verbose_name='Category Scheme', on_delete=models.CASCADE, related_name='categories')

class Categorization(MaintainableArtefact):
    source = models.ForeignKey(ReferenceObject)
    target = models.ForeignKey(Category)

class ReportingTaxonomy(MaintainableArtefact):
    pass

class ReportingCategory(Item):
    wrapper = models.ForeignKey(ReportingTaxonomy, verbose_name='Reporting Taxonomy', on_delete=models.CASCADE, related_name='categories')
    dsds = models.ManyToManyField(DataStructure) 
    metadsds = models.ManyToManyField(MetadataStructure)
    dataflows = models.ManyToManyField(Dataflow)
    metadataflows = models.ManyToManyField(Metadataflow) 
