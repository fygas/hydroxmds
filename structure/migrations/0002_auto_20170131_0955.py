# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textformatinfo',
            name='textType',
            field=models.CharField(blank=True, choices=[('AlphaNumeric', 'AlphaNumeric'), ('StandardTimePeriod', 'StandardTimePeriod'), ('BasicTimePeriod', 'BasicTimePeriod'), ('GregorianYearMonth', 'GregorianYearMonth'), ('ReportingTimePeriod', 'ReportingTimePeriod'), ('ReportingQuarter', 'ReportingQuarter'), ('GregorianDay', 'GregorianDay'), ('ReportingYear', 'ReportingYear'), ('DateTime', 'DateTime'), ('TimeRange', 'TimeRange'), ('Time', 'Time'), ('ReportingMonth', 'ReportingMonth'), ('XHTML', 'XHTML'), ('BigInteger', 'BigInteger'), ('Float', 'Float'), (None, 'None'), ('ReportingSemester', 'ReportingSemester'), ('ReportingTrimester', 'ReportingTrimester'), ('IdentifiableReference', 'IdentifiableReference'), ('Incremental', 'Incremental'), ('Alpha', 'Alpha'), ('Count', 'Count'), ('Numeric', 'Numeric'), ('String', 'String'), ('Duration', 'Duration'), ('Boolean', 'Boolean'), ('Integer', 'Integer'), ('GregorianYear', 'GregorianYear'), ('AttachmentConstraintReference', 'AttachmentConstraintReference'), ('Short', 'Short'), ('URI', 'URI'), ('ExclusiveValueRange', 'ExclusiveValueRange'), ('ReportingDay', 'ReportingDay'), ('KeyValues', 'KeyValues'), ('Decimal', 'Decimal'), ('Double', 'Double'), ('GregorianTimePeriod', 'GregorianTimePeriod'), ('ReportingWeek', 'ReportingWeek'), ('DataSetReference', 'DataSetReference'), ('Month', 'Month'), ('MonthDay', 'MonthDay'), ('InclusiveValueRange', 'InclusiveValueRange'), ('Long', 'Long'), ('Day', 'Day'), ('ObservationalTimePeriod', 'ObservationalTimePeriod')], max_length=18, null=True),
        ),
    ]