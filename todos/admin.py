from django.contrib import admin

# Register your models here.
from django.contrib import admin
from todos.models import List

admin.site.register(List)