# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('comments', models.TextField(default=b'', max_length=300, blank=True)),
                ('date_added', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('shop', models.ForeignKey(to='manager.Shop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
