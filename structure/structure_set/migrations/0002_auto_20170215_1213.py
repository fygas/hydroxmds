# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure_set', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='categorymaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='categoryschememaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='codelistmaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='codemaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='componentmaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='conceptmaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='conceptschememaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='hybridcodelistmap',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='hybridcodemaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='organisationmaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='organisationschememaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymaptranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='structuremap',
            name='id_code',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='agencyID',
            field=models.CharField(max_length=18, verbose_name='agencyID'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='id_code',
            field=models.CharField(max_length=18, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='isExternalReference',
            field=models.BooleanField(default=False, verbose_name='isExternalReference'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='isFinal',
            field=models.BooleanField(default=False, verbose_name='isFinal'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='validFrom',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validFrom'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='validTo',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validTo'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='version',
            field=models.CharField(default='1.0', max_length=18, verbose_name='version'),
        ),
        migrations.AlterField(
            model_name='structuresettranslation',
            name='Name',
            field=models.CharField(max_length=18),
        ),
    ]