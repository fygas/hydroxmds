# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataflow',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Reference'),
        ),
    ]
