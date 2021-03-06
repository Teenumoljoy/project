# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0012_remove_orderdetail_event_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='event_type',
        ),
    ]
