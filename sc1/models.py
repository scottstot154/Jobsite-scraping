from django.db import models

class Jobs(models.Model):
	task = models.CharField(max_length=100)
	company = models.CharField(max_length=100,null=True,blank=True)
	details = models.TextField(max_length=200, blank=True, null=True)
	location = models.CharField(max_length=200)
	salary = models.CharField(max_length=100, default='NA')
	begin = models.CharField(max_length=20, blank=True)
	duration = models.CharField(max_length=10, blank=True)
