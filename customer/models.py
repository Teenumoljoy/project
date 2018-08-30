# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	usr_data  = models.OneToOneField(User)
	phonenumber=models.IntegerField()
	address = models.TextField(max_length=100)
	district = models.CharField(max_length=100)
	zipcode= models.IntegerField()
	profilepic=models.ImageField(upload_to='media/profilepic/')
	creaed_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.usr_data.first_name+' '+self.usr_data.last_name
