# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0015_auto_20170228_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisationtranslation',
            name='Name',
        ),
        migrations.AlterField(
            model_name='organisationtranslation',
            name='name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
