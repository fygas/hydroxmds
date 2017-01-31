# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_auto_20170131_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textformatinfo',
            name='textType',
            field=models.CharField(blank=True, choices=[('BasicTimePeriod', 'BasicTimePeriod'), ('Boolean', 'Boolean'), ('TimeRange', 'TimeRange'), ('String', 'String'), ('Short', 'Short'), ('Count', 'Count'), ('ReportingSemester', 'ReportingSemester'), ('Alpha', 'Alpha'), ('ObservationalTimePeriod', 'ObservationalTimePeriod'), ('Integer', 'Integer'), ('ReportingTimePeriod', 'ReportingTimePeriod'), ('XHTML', 'XHTML'), ('AttachmentConstraintReference', 'AttachmentConstraintReference'), ('MonthDay', 'MonthDay'), ('KeyValues', 'KeyValues'), ('ReportingDay', 'ReportingDay'), ('Duration', 'Duration'), ('AlphaNumeric', 'AlphaNumeric'), ('ReportingMonth', 'ReportingMonth'), ('Long', 'Long'), ('GregorianYearMonth', 'GregorianYearMonth'), ('Float', 'Float'), ('ReportingWeek', 'ReportingWeek'), ('DateTime', 'DateTime'), ('Time', 'Time'), ('BigInteger', 'BigInteger'), ('DataSetReference', 'DataSetReference'), ('ReportingYear', 'ReportingYear'), ('ReportingTrimester', 'ReportingTrimester'), ('Month', 'Month'), (None, 'None'), ('Double', 'Double'), ('ExclusiveValueRange', 'ExclusiveValueRange'), ('GregorianYear', 'GregorianYear'), ('Day', 'Day'), ('URI', 'URI'), ('Incremental', 'Incremental'), ('ReportingQuarter', 'ReportingQuarter'), ('InclusiveValueRange', 'InclusiveValueRange'), ('StandardTimePeriod', 'StandardTimePeriod'), ('GregorianDay', 'GregorianDay'), ('Numeric', 'Numeric'), ('IdentifiableReference', 'IdentifiableReference'), ('GregorianTimePeriod', 'GregorianTimePeriod'), ('Decimal', 'Decimal')], max_length=18, null=True),
        ),
    ]
