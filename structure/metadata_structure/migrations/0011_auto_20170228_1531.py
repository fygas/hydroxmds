# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata_structure', '0010_auto_20170228_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadatastructure',
            name='isExternalReference',
        ),
        migrations.RemoveField(
            model_name='metadatastructure',
            name='urn',
        ),
        migrations.RemoveField(
            model_name='metadatatarget',
            name='urn',
        ),
        migrations.RemoveField(
            model_name='metadatatargetlist',
            name='urn',
        ),
        migrations.RemoveField(
            model_name='reportstructure',
            name='urn',
        ),
        migrations.RemoveField(
            model_name='reportstructurelist',
            name='urn',
        ),
        migrations.AlterField(
            model_name='metadatastructure',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_metadatastructure_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='metadatatarget',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_metadatatarget_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='metadatatargetlist',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_metadatatargetlist_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='reportstructure',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_reportstructure_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='reportstructurelist',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_reportstructurelist_annotations_+', to='common.Annotation'),
        ),
    ]
