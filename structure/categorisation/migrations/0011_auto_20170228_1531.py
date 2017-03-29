# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorisation', '0010_auto_20170228_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorisation',
            name='isExternalReference',
        ),
        migrations.RemoveField(
            model_name='categorisation',
            name='urn',
        ),
        migrations.AlterField(
            model_name='categorisation',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_categorisation_annotations_+', to='common.Annotation'),
        ),
    ]
