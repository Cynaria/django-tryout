from django.db import models

# Create your models here.


class List(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField()
