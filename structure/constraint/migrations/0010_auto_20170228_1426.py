# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constraint', '0009_auto_20170228_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraintartefact',
            name='annotations',
            field=models.ManyToManyField(null=True, related_name='_constraintartefact_annotations_+', to='common.Annotation'),
        ),
    ]
