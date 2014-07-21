from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from todos.models import List

# Create your views here.

def index(request):
	todo_lists = List.objects.all()[:5]
	template = loader.get_template('todos/index.html')
	context = RequestContext(request, {'todo_lists': todo_lists})
	return HttpResponse(template.render(context))

def detail(request,list_id):
	list = get_object_or_404(List, pk=list_id)
	print(list.item_set.all())
	template = loader.get_template('todos/details.html')
	context = RequestContext(request, {'list': list})
	return HttpResponse(template.render(context))
