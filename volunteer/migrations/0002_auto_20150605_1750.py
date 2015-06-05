# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='addressL1',
        ),
        migrations.RemoveField(
            model_name='text',
            name='addressL2',
        ),
        migrations.RemoveField(
            model_name='text',
            name='email',
        ),
        migrations.RemoveField(
            model_name='text',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='text',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='text',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='text',
            name='town',
        ),
    ]
