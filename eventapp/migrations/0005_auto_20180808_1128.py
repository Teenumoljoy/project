# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0004_auto_20180808_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='event_date',
            field=models.DateField(null=True),
        ),
    ]
