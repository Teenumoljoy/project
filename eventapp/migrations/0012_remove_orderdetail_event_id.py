# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0011_remove_orderdetail_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='event_id',
        ),
    ]
