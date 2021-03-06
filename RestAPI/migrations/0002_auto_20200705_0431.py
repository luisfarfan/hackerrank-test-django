# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-07-05 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='repo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
