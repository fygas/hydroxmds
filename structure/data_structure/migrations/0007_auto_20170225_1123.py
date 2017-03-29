# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 09:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170225_1123'),
        ('data_structure', '0006_auto_20170225_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datastructuretranslation',
            old_name='Description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='datastructure',
            name='Annotations',
        ),
        migrations.AddField(
            model_name='datastructure',
            name='annotations',
            field=models.ManyToManyField(related_name='_datastructure_annotations_+', to='common.Annotation'),
        ),
        migrations.AddField(
            model_name='datastructuretranslation',
            name='name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='datastructure',
            name='id_code',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]
