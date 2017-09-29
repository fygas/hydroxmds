# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydro_sdmx', '0011_auto_20170924_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textformatinfo',
            name='text_type',
            field=models.CharField(blank=True, choices=[('Time', 'Time'), ('BigInteger', 'BigInteger'), ('URI', 'URI'), ('Long', 'Long'), ('ExclusiveValueRange', 'ExclusiveValueRange'), ('InclusiveValueRange', 'InclusiveValueRange'), ('Incremental', 'Incremental'), ('Alpha', 'Alpha'), ('String', 'String'), ('GregorianYear', 'GregorianYear'), ('ReportingYear', 'ReportingYear'), ('TimeRange', 'TimeRange'), ('Month', 'Month'), ('GregorianDay', 'GregorianDay'), ('XHTML', 'XHTML'), ('AttachmentConstraintReference', 'AttachmentConstraintReference'), ('Integer', 'Integer'), ('BasicTimePeriod', 'BasicTimePeriod'), ('MonthDay', 'MonthDay'), ('ReportingDay', 'ReportingDay'), (None, 'None'), ('GregorianYearMonth', 'GregorianYearMonth'), ('KeyValues', 'KeyValues'), ('IdentifiableReference', 'IdentifiableReference'), ('Numeric', 'Numeric'), ('DateTime', 'DateTime'), ('ReportingMonth', 'ReportingMonth'), ('ReportingWeek', 'ReportingWeek'), ('Short', 'Short'), ('GregorianTimePeriod', 'GregorianTimePeriod'), ('Boolean', 'Boolean'), ('AlphaNumeric', 'AlphaNumeric'), ('StandardTimePeriod', 'StandardTimePeriod'), ('Float', 'Float'), ('Double', 'Double'), ('ReportingSemester', 'ReportingSemester'), ('ReportingTrimester', 'ReportingTrimester'), ('ReportingTimePeriod', 'ReportingTimePeriod'), ('Day', 'Day'), ('Decimal', 'Decimal'), ('Duration', 'Duration'), ('DataSetReference', 'DataSetReference'), ('ReportingQuarter', 'ReportingQuarter'), ('Count', 'Count'), ('ObservationalTimePeriod', 'ObservationalTimePeriod')], max_length=63),
        ),
    ]
