# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchical_codelist', '0008_auto_20170228_1104'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hierarchicalcodelist',
            unique_together=set([('id_code', 'agencyID', 'version')]),
        ),
    ]
