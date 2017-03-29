# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 09:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170225_1123'),
        ('reporting_taxonomy', '0006_auto_20170225_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportingcategorytranslation',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='reportingtaxonomytranslation',
            old_name='Description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='reportingcategory',
            name='Annotations',
        ),
        migrations.RemoveField(
            model_name='reportingtaxonomy',
            name='Annotations',
        ),
        migrations.AddField(
            model_name='reportingcategory',
            name='annotations',
            field=models.ManyToManyField(related_name='_reportingcategory_annotations_+', to='common.Annotation'),
        ),
        migrations.AddField(
            model_name='reportingcategorytranslation',
            name='name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='reportingtaxonomy',
            name='annotations',
            field=models.ManyToManyField(related_name='_reportingtaxonomy_annotations_+', to='common.Annotation'),
        ),
        migrations.AddField(
            model_name='reportingtaxonomytranslation',
            name='name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='reportingcategory',
            name='id_code',
            field=models.CharField(default='id_add', max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportingtaxonomy',
            name='id_code',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
        ),
    ]
