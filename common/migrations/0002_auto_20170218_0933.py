# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='uri',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='urn',
        ),
        migrations.AlterField(
            model_name='annotation',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
    ]
