# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0008_auto_20180809_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='myevent',
            name='booking_date',
            field=models.DateField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
