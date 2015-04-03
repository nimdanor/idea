# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import concept.LowerCharField


class Migration(migrations.Migration):

    dependencies = [
        ('concept', '0002_auto_20150212_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='name',
            field=concept.LowerCharField.LowerCaseCharField(unique=True, max_length=30, verbose_name='Le nom du concept'),
            preserve_default=True,
        ),
    ]
