# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 07:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import re


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170225_1123'),
        ('organisation', '0007_auto_20170225_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.URLField(blank=True, null=True)),
                ('uri', models.URLField(blank=True, null=True)),
                ('version', models.CharField(default='1.0', max_length=18, validators=[django.core.validators.RegexValidator(re.compile('[0-9]+(\\.[0-9]+)*', 32), 'Enter a value of type VersionType that has pattern "([0-9]+(\\.[0-9]+)*)"', 'invalid_pattern')])),
                ('validFrom', models.DateTimeField(blank=True, null=True)),
                ('validTo', models.DateTimeField(blank=True, null=True)),
                ('agencyID', models.CharField(max_length=18)),
                ('isFinal', models.BooleanField(default=False)),
                ('isExternalReference', models.BooleanField(default=False)),
                ('isPartial', models.BooleanField(default=False)),
                ('id_code', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id')),
                ('annotations', models.ManyToManyField(related_name='_organisationscheme_annotations_+', to='common.Annotation')),
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
            name='OrganisationSchemeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=18, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('Name', models.CharField(max_length=18)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='organisation.OrganisationScheme')),
            ],
            options={
                'db_table': 'organisation_organisationscheme_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Fax',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Telephone',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='URI',
            new_name='uRI',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='X400',
            new_name='x400',
        ),
        migrations.RenameField(
            model_name='contacttranslation',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='contacttranslation',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contacttranslation',
            old_name='Role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='Parent',
            new_name='parent',
        ),
        migrations.AddField(
            model_name='contact',
            name='id_code',
            field=models.CharField(default=0, max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='organisation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisationtranslation',
            name='Name',
            field=models.CharField(default=0, max_length=18),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='id_code',
            field=models.CharField(default=0, max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z0-9_@$\\-]+', 32), 'Enter a value of type IDType that has pattern "([A-Za-z0-9_@$\\-]+)"', 'invalid_pattern')], verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisationScheme',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organisation.OrganisationScheme'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='Contacts',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='type_code',
        ),
        migrations.AlterUniqueTogether(
            name='organisation',
            unique_together=set([('organisationScheme', 'id_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='organisationschemetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
