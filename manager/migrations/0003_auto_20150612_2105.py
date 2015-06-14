# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_commodity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={'verbose_name_plural': 'Commodities'},
        ),
    ]
