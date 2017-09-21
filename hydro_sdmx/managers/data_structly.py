
from django.db import models

class DataStructlyDimensionManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return qs.prefetch_related('dimensions')

class WrapperConceptManager(models.Manager):
    def get_queryset(self):
        super_qs = super().get_queryset()
        return qs.select_related('concept', 'wrapper')

