# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('comments', models.TextField(default=b'', max_length=300, blank=True)),
                ('date_added', models.DateTimeField(default=datetime.date(2015, 6, 14), auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Commodities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('oxfamID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('telephone', models.TextField()),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('addressL1', models.TextField(default=b'')),
                ('addressL2', models.TextField(blank=True)),
                ('postcode', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='commodity',
            name='shop',
            field=models.ForeignKey(to='manager.Shop'),
            preserve_default=True,
        ),
    ]
