# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerapplication',
            old_name='birthday',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='health_and_safety',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference1_received',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference1_sent',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference2_received',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference2_sent',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='risk_assessment',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='start_date',
        ),
    ]
