# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class MyEvent(models.Model):
	CATEGORY_CHOICES =(    ('WEDDING', 'WEDDING'),
                          ('PHOTOGRAPHY', 'PHOTOGRAPHY'),
                          ('VIDEOGRAPHY','VIDEOGRAPHY'),
                          ('DECORATION','DECORATION')
                       )
	event_type= models.CharField(max_length=100, choices=CATEGORY_CHOICES)
	event_name=models.CharField(max_length=100)
	pic=models.ImageField(upload_to='media/eventpics/',null=True,blank=True)
	rate=models.IntegerField()
	booking_date=models.DateField(auto_now=True)
	event_date=models.DateField(null=True,blank=True)
	created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.event_name

class OrderDetail(models.Model):
	booked_by=models.ForeignKey(User)
	event_type=models.CharField(max_length=100)
	event_name=models.CharField(max_length=100)
	event_date=models.DateField(null=False)
	def __str__(self):
		return self.event_name

	








