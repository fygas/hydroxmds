# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0019_auto_20170228_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='urn',
        ),
        migrations.RemoveField(
            model_name='componentlist',
            name='urn',
        ),
        migrations.AlterField(
            model_name='component',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_component_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='componentlist',
            name='annotations',
            field=models.ManyToManyField(blank=True, null=True, related_name='_componentlist_annotations_+', to='common.Annotation'),
        ),
        migrations.AlterField(
            model_name='textformatinfo',
            name='textType',
            field=models.CharField(blank=True, choices=[('KeyValues', 'KeyValues'), ('Alpha', 'Alpha'), ('BigInteger', 'BigInteger'), ('ObservationalTimePeriod', 'ObservationalTimePeriod'), ('DateTime', 'DateTime'), ('TimeRange', 'TimeRange'), ('Day', 'Day'), ('Integer', 'Integer'), ('Short', 'Short'), ('GregorianYear', 'GregorianYear'), ('ReportingMonth', 'ReportingMonth'), ('ReportingTrimester', 'ReportingTrimester'), ('ReportingWeek', 'ReportingWeek'), ('GregorianYearMonth', 'GregorianYearMonth'), ('Duration', 'Duration'), ('Double', 'Double'), ('InclusiveValueRange', 'InclusiveValueRange'), ('ReportingQuarter', 'ReportingQuarter'), ('DataSetReference', 'DataSetReference'), ('Month', 'Month'), ('XHTML', 'XHTML'), ('Count', 'Count'), ('URI', 'URI'), ('MonthDay', 'MonthDay'), ('IdentifiableReference', 'IdentifiableReference'), ('ReportingDay', 'ReportingDay'), ('AttachmentConstraintReference', 'AttachmentConstraintReference'), (None, 'None'), ('ReportingYear', 'ReportingYear'), ('Boolean', 'Boolean'), ('ExclusiveValueRange', 'ExclusiveValueRange'), ('StandardTimePeriod', 'StandardTimePeriod'), ('Numeric', 'Numeric'), ('String', 'String'), ('Float', 'Float'), ('GregorianTimePeriod', 'GregorianTimePeriod'), ('AlphaNumeric', 'AlphaNumeric'), ('Decimal', 'Decimal'), ('Incremental', 'Incremental'), ('BasicTimePeriod', 'BasicTimePeriod'), ('GregorianDay', 'GregorianDay'), ('ReportingTimePeriod', 'ReportingTimePeriod'), ('Time', 'Time'), ('Long', 'Long'), ('ReportingSemester', 'ReportingSemester')], max_length=255, null=True),
        ),
    ]
