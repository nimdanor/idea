# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pldata', '0002_auto_20160413_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pldata',
            name='stamp',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True, verbose_name='time'),
        ),
    ]
