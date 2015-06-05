# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.IntegerField(default=1, serialize=False, primary_key=True)),
                ('mission', models.TextField()),
                ('description', models.TextField()),
                ('donate', models.TextField()),
                ('getinvolved', models.TextField()),
                ('addressL1', models.TextField()),
                ('addressL2', models.TextField()),
                ('postcode', models.CharField(max_length=10)),
                ('town', models.TextField()),
                ('telephone', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
