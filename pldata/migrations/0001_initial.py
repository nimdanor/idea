# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pldata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('stamp', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='time')),
                ('data', models.TextField(default='{}', verbose_name='jsondata')),
            ],
        ),
    ]
