from django.db import models
from hydro_sdmx.models import Code

# Create your models here.

class OrgEvolution(models.Model):
    birth = models.DateField()
    close = models.DateField(null=True, blank=True)

class OrgIdMap(models.Model):
    id_type = models.ForeignKey(Code, on_delete=models.CASCADE)
    id_code = models.CharField(max_length=255)
    org = models.ForeignKey(OrgEvolution)

class OrgEvolutionIn(models.Model):
    org = models.ForeignKey(OrgEvolution, on_delete=models.CASCADE)
    birth = models.DateField()
    close = models.DateField(null=True, blank=True)
    source = models.ForeignKey(OrgEvolution, on_delete=models.CASCADE)

class OrgPropertiesIn(models.Model):
    org = models.ForeignKey(OrgEvolutionIn, on_delete=models.CASCADE)
    source = models.ForeignKey(OrgEvolution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    valid_from = models.DateTimeField()

class OrgProperties(models.Model):
    org = models.ForeignKey(OrgEvolution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    valid_from = models.DateTimeField()

class OrgIds(models.Model):
    pass

