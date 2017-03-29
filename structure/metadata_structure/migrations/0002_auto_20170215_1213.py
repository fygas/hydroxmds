# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata_structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadatastructure',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='metadatastructuretranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='metadatatarget',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='metadatatargetlist',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportstructure',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportstructurelist',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
    ]
