# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataflow', '0002_auto_20170131_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataflow',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
    ]
