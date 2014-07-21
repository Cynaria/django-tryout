from django.db import models

# Create your models here.


class List(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField()
	def __str__(self):
		return self.title


class Item(models.Model):
	name = models.CharField(max_length=140)
	description = models.TextField()
	list = models.ForeignKey(List)
	completed = models.BooleanField(default = False)
	def __str__(self):
		return self.name