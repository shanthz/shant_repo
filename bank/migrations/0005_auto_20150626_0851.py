# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20150626_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_opened',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 26, 8, 51, 50, 627691)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 26, 8, 51, 50, 627083)),
            preserve_default=True,
        ),
    ]