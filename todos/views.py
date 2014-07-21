from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from todos.models import List

# Create your views here.

def index(request):
	todo_lists = List.objects.all()[:5]
	template = loader.get_template('todos/index.html')
	context = RequestContext(request, {'todo_lists': todo_lists})
	return HttpResponse(template.render(context))