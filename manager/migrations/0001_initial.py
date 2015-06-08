# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('address', models.TextField(default=b'', max_length=300, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
