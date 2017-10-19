from django.db import models

from ..settings import api_maxlen_settings as maxlengths

class Dataset(models.Model):
    dataflow = models.OneToOneField('Dataflow', on_delete=models.CASCADE)

class Documentation(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='singletons')
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    code_value = models.ForeignKey('Code', null=True, blank=True, on_delete=models.CASCADE)
    string_value = models.CharField(max_length=255, blank=True)
    registration = models.ForeignKey('Registration', on_delete=models.CASCADE, editable=False, related_name='+')

    class Meta:
        abstract=True
        unique_together = ('dataset', 'attribute', 'registration')

class DatasetAttribute(Documentation):
    pass

class DimensionLevelAttribute(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    key = models.ForeignKey('Key', on_delete=models.CASCADE, related_name='+')

class Obs(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='singletons')
    series = models.ForeignKey('Key', on_delete=models.CASCADE)
    measure = models.ForeignKey('key', on_delete=models.CASCADE, null=True, blank=True)
    time = models.ForeignKey('Time', on_delete=models.CASCADE)
    obs_value = models.CharField(max_length=maxlengths.OBS_VALUE)
    registration = models.ForeignKey('Registration', on_delete=models.CASCADE, editable=False, related_name='+')

class ObsAttribute(Documentation):
    dataset=None
