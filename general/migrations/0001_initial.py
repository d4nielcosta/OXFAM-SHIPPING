# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.IntegerField(default=1, serialize=False, primary_key=True)),
                ('intro', models.TextField()),
                ('mission', models.TextField()),
                ('description', models.TextField()),
                ('volunteer', models.TextField()),
                ('donate', models.TextField()),
                ('footerdonate', models.TextField()),
                ('location', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forename', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('role', models.TextField()),
                ('emergency_contact_forename', models.CharField(default=b'NO FORENAME ENTERED', max_length=128)),
                ('emergency_contact_surname', models.CharField(default=b'NO SURNAME ENTERED', max_length=128)),
                ('emergency_contact_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('address', models.TextField(default=b'', max_length=300, blank=True)),
                ('reference1_forename', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference1_surname', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference1_primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('reference1_secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('reference1_email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('reference1_sent', models.BooleanField(default=False)),
                ('reference1_received', models.BooleanField(default=False)),
                ('reference2_forename', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference2_surname', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference2_primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('reference2_secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999")])),
                ('reference2_email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('reference2_sent', models.BooleanField(default=False)),
                ('reference2_received', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=datetime.date(2015, 5, 25), blank=True)),
                ('birthday', models.DateField()),
                ('risk_assessment', models.BooleanField(default=False)),
                ('health_and_safety', models.BooleanField(default=False)),
                ('parental_permission', models.BooleanField(default=False)),
                ('permission_to_work', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
