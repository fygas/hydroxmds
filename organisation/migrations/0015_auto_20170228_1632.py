# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 14:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0014_auto_20170228_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisationscheme',
            name='isPartial',
        ),
        migrations.AlterField(
            model_name='organisationscheme',
            name='id_code',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[A-Za-z0-9_@$\\-]+$', 32), 'Enter a value of type IDType that has pattern "(^[A-Za-z0-9_@$\\-]+$)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]