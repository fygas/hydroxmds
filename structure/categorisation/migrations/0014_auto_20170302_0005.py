# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorisation', '0013_auto_20170228_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorisation',
            name='annotations',
            field=models.ManyToManyField(blank=True, related_name='_categorisation_annotations_+', to='common.Annotation'),
        ),
    ]
