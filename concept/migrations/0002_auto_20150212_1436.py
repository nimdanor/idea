# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concept', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='ascendant',
            field=models.ForeignKey(to='concept.Concept', related_name='prerequis'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='descendant',
            field=models.ForeignKey(to='concept.Concept', related_name='element'),
            preserve_default=True,
        ),
    ]
