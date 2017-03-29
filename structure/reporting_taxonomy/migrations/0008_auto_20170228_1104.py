# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 09:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_taxonomy', '0007_auto_20170225_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingcategory',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingcategorytranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingcategorytranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomy',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomy',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomy',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomytranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomytranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
