# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pldata.models


class Migration(migrations.Migration):

    dependencies = [
        ('pldata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pldata',
            name='stamp',
            field=models.DateTimeField(verbose_name='time', blank=True, default=pldata.models.mynow),
        ),
    ]
