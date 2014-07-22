from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class List(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField()
	creator = models.ForeignKey(User)
	def __str__(self):
		return self.title

	def completed_list_items(self):
		return self.item_set.filter(completed = True)

	def uncompleted_list_items(self):
		return self.item_set.filter(completed = False)

class Item(models.Model):
	name = models.CharField(max_length=140)
	description = models.TextField()
	list = models.ForeignKey(List)
	completed = models.BooleanField(default = False)
	def __str__(self):
		return self.name