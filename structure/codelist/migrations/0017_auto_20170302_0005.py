# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 22:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('codelist', '0016_auto_20170301_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='annotations',
            field=models.ManyToManyField(blank=True, related_name='_code_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='annotations',
            field=models.ManyToManyField(blank=True, related_name='_codelist_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='id_code',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z][A-Za-z0-9_\\-]*', 32), 'Enter a value of type NCNameIDType that has pattern "([A-Za-z][A-Za-z0-9_\\-]*)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]