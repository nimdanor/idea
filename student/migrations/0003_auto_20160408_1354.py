# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20160408_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='concepts',
        ),
        migrations.AddField(
            model_name='student',
            name='conceptjson',
            field=models.TextField(default={'root': 4}),
            preserve_default=False,
        ),
    ]
