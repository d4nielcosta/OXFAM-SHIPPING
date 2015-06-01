# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20150527_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference1_secondary_phone',
        ),
        migrations.RemoveField(
            model_name='volunteerapplication',
            name='reference2_secondary_phone',
        ),
        migrations.AddField(
            model_name='volunteerapplication',
            name='email',
            field=models.EmailField(default='something@aol.com', max_length=75),
            preserve_default=False,
        ),
    ]
