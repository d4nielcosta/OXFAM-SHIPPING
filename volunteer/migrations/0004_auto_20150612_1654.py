# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_text_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='name',
            field=models.CharField(default=b'texts for volunteers page', max_length=128),
        ),
    ]
