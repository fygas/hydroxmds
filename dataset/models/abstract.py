from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseDataset(models.Model):
    delete = models.BooleanField(default=False)
    timestamp = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
