from django.db import models
from common.models import Reference, TextFormat

class Representation(models.Model):
    TextFormat = models.ForeignKey(TextFormat, on_delete=models.CASCADE, null=True, blank=True)
    Enumeration = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True, blank=True)
    EnumerationFormat = models.ForeignKey(TextFormat, on_delete=models.CASCADE, null=True, blank=True)
