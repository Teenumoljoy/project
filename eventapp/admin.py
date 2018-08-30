# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from eventapp.models import MyEvent,OrderDetail
# Register your models here.

admin.site.register(MyEvent)
admin.site.register(OrderDetail)
