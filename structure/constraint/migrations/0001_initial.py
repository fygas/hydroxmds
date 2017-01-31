# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:09
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
            name='ConstraintArtefact',
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
                ('type_code', models.CharField(blank=True, choices=[(None, 'None'), ('Attachment', 'Attachmetn'), ('Content', 'Content')], max_length=18, null=True)),
                ('Annotations', models.ManyToManyField(related_name='_constraintartefact_Annotations_+', to='common.Annotation')),
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
            name='ConstraintArtefactTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=18, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='constraint.ConstraintArtefact')),
            ],
            options={
                'db_table': 'constraint_constraintartefact_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ConstraintAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataProvider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.Reference')),
                ('DataSet', models.ManyToManyField(related_name='_constraintattachment_DataSet_+', to='common.Reference')),
                ('DataStructure', models.ManyToManyField(related_name='_constraintattachment_DataStructure_+', to='common.Reference')),
                ('Dataflow', models.ManyToManyField(related_name='_constraintattachment_Dataflow_+', to='common.Reference')),
                ('MetadataSet', models.ManyToManyField(related_name='_constraintattachment_MetadataSet_+', to='common.Reference')),
                ('MetadataStructure', models.ManyToManyField(related_name='_constraintattachment_MetadataStructure_+', to='common.Reference')),
                ('Metadataflow', models.ManyToManyField(related_name='_constraintattachment_Metadataflow_+', to='common.Reference')),
                ('ProvisionAgreement', models.ManyToManyField(related_name='_constraintattachment_ProvisionAgreement_+', to='common.Reference')),
                ('QueryableDataSource', models.ManyToManyField(related_name='_constraintattachment_QueryableDataSource_+', to='common.QueryableDataSource')),
                ('SimpleDataSource', models.ManyToManyField(related_name='_constraintattachment_SimpleDataSource_+', to='common.Reference')),
            ],
        ),
        migrations.CreateModel(
            name='KeySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isIncluded', models.NullBooleanField()),
                ('Keys', models.ManyToManyField(related_name='_keyset_Keys_+', to='common.Key')),
            ],
        ),
        migrations.AddField(
            model_name='constraintartefact',
            name='ConstraintAttachment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='constraint.ConstraintAttachment'),
        ),
        migrations.AddField(
            model_name='constraintartefact',
            name='CubeRegion',
            field=models.ManyToManyField(related_name='_constraintartefact_CubeRegion_+', to='common.Key'),
        ),
        migrations.AddField(
            model_name='constraintartefact',
            name='DataKeySet',
            field=models.ManyToManyField(related_name='_constraintartefact_DataKeySet_+', to='constraint.KeySet'),
        ),
        migrations.AddField(
            model_name='constraintartefact',
            name='MetadataKeySet',
            field=models.ManyToManyField(related_name='_constraintartefact_MetadataKeySet_+', to='constraint.KeySet'),
        ),
        migrations.AlterUniqueTogether(
            name='constraintartefacttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
