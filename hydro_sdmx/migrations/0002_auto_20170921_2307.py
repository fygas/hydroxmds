# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydro_sdmx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='uri',
            field=models.URLField(blank=True, null=True, verbose_name='URI'),
        ),
    ]
