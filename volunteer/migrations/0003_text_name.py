# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20150605_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='name',
            field=models.TextField(default=b'texts for volunteers page'),
            preserve_default=True,
        ),
    ]
