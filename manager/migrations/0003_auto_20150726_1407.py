# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_shop_randomletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='id',
        ),
        migrations.AddField(
            model_name='commodity',
            name='ref_number',
            field=models.CharField(default=datetime.date(2015, 7, 26), max_length=128, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commodity',
            name='date_added',
            field=models.DateTimeField(default=datetime.date(2015, 7, 26), auto_now=True, auto_now_add=True),
        ),
    ]
