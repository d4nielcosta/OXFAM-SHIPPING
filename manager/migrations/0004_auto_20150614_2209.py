# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20150612_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='date_added',
            field=models.DateTimeField(default=datetime.date(2015, 6, 14), auto_now=True, auto_now_add=True),
        ),
    ]
