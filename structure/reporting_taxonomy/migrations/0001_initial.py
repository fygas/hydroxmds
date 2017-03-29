# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.URLField(blank=True, null=True)),
                ('uri', models.URLField(blank=True, null=True)),
                ('id_code', models.CharField(blank=True, max_length=18, null=True)),
                ('Annotations', models.ManyToManyField(related_name='_reportingcategory_Annotations_+', to='common.Annotation')),
                ('ProvisioningMetadata', models.ManyToManyField(related_name='_reportingcategory_ProvisioningMetadata_+', to='common.Reference')),
                ('ReportingCategories', models.ManyToManyField(related_name='_reportingcategory_ReportingCategories_+', to='reporting_taxonomy.ReportingCategory')),
                ('StructuralMetadata', models.ManyToManyField(related_name='_reportingcategory_StructuralMetadata_+', to='common.Reference')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ReportingCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=18, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='reporting_taxonomy.ReportingCategory')),
            ],
            options={
                'db_table': 'reporting_taxonomy_reportingcategory_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ReportingTaxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.URLField(blank=True, null=True)),
                ('uri', models.URLField(blank=True, null=True)),
                ('id_code', models.CharField(blank=True, max_length=18, null=True)),
                ('version', models.CharField(blank=True, max_length=18, null=True)),
                ('validFrom', models.DateTimeField(blank=True, null=True)),
                ('validTo', models.DateTimeField(blank=True, null=True)),
                ('agencyID', models.CharField(blank=True, max_length=18, null=True)),
                ('isFinal', models.BooleanField(default=False)),
                ('isExternalReference', models.BooleanField(default=False)),
                ('isPartial', models.BooleanField(default=False)),
                ('Annotations', models.ManyToManyField(related_name='_reportingtaxonomy_Annotations_+', to='common.Annotation')),
                ('ReportingCategories', models.ManyToManyField(related_name='_reportingtaxonomy_ReportingCategories_+', to='reporting_taxonomy.ReportingCategory')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ReportingTaxonomyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=18, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='reporting_taxonomy.ReportingTaxonomy')),
            ],
            options={
                'db_table': 'reporting_taxonomy_reportingtaxonomy_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='reportingtaxonomytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='reportingcategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]