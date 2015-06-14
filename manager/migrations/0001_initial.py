# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('tracknumber', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('oxfamID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('manager', models.TextField()),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('phonenumber', models.TextField()),
                ('addressL1', models.TextField(default=b'')),
                ('addressL2', models.TextField(default=b'', blank=True)),
                ('postcode', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
