# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 09:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('structure_set', '0007_auto_20170225_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='categorymap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='categorymaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categorymaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='categoryschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='categoryschememaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categoryschememaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='codelistmap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='codelistmaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='codelistmaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='codemap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='codemaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='codemaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='componentmap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='componentmaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='componentmaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='conceptmap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='conceptmaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='conceptmaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='conceptschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='conceptschememaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='conceptschememaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hybridcodelistmap',
            name='id_code',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='hybridcodelistmaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='hybridcodemap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='hybridcodemaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hybridcodemaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='organisationmap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='organisationmaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationmaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='organisationschememap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='organisationschememaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationschememaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingcategorymap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='reportingcategorymaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingcategorymaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymap',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymaptranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reportingtaxonomymaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='structuremap',
            name='id_code',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='structuremaptranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='agencyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='id_code',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='structureset',
            name='version',
            field=models.CharField(default='1.0', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')]),
        ),
        migrations.AlterField(
            model_name='structuresettranslation',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='structuresettranslation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]