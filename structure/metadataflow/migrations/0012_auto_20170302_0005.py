# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadataflow', '0011_auto_20170228_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataflow',
            name='annotations',
            field=models.ManyToManyField(blank=True, related_name='_metadataflow_annotations_+', to='common.Annotation'),
        ),
    ]