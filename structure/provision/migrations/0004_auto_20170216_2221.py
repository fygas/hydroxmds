# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provision', '0003_auto_20170215_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provision',
            name='agencyID',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='provision',
            name='isExternalReference',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='provision',
            name='isFinal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='provision',
            name='uri',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provision',
            name='urn',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provision',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provision',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provision',
            name='version',
            field=models.CharField(default='1.0', max_length=18),
        ),
    ]
