# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0016_auto_20180810_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='eventpics/'),
        ),
    ]