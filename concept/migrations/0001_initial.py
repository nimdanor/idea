# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Le nom du concept')),
                ('lname', models.CharField(max_length=300, blank=True, verbose_name='Long Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('update', models.DateTimeField(verbose_name='date update', auto_now=True)),
                ('level', models.IntegerField(default=-1, verbose_name='niveau')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, default='prerequisite', verbose_name='Le type du lien')),
                ('ascendant', models.ForeignKey(to='concept.Concept', related_name='from')),
                ('descendant', models.ForeignKey(to='concept.Concept', related_name='to')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='concept',
            name='link',
            field=models.ManyToManyField(through='concept.Link', to='concept.Concept'),
            preserve_default=True,
        ),
    ]
