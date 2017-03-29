# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 09:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_auto_20170218_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]
