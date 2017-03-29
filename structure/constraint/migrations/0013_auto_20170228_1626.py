# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 14:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('constraint', '0012_auto_20170228_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraintartefact',
            name='id_code',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[A-Za-z0-9_@$\\-]+$', 32), 'Enter a value of type IDType that has pattern "(^[A-Za-z0-9_@$\\-]+$)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]