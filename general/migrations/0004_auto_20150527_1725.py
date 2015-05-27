# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_remove_text_volunteer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='adreessL1',
            new_name='addressL1',
        ),
    ]
