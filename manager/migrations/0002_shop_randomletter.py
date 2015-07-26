# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='randomletter',
            field=models.CharField(default='a', max_length=1),
            preserve_default=False,
        ),
    ]
