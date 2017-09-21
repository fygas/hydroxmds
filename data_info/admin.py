from .models import DataStructure, Group, Dimension, ObsValue, Attribute, DataConstraint 

from django.contrib import admin

for model in [DataStructure, Group, Dimension, ObsValue, Attribute, DataConstraint]:
    admin.site.register(model)
