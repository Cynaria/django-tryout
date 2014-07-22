from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from todos.models import List, Item

# Create your views here.

def index(request):
	todo_lists = List.objects.all()[:5]
	template = loader.get_template('todos/index.html')
	context = RequestContext(request, {'todo_lists': todo_lists})
	return HttpResponse(template.render(context))

def detail(request,list_id):
	list = get_object_or_404(List, pk=list_id)
	template = loader.get_template('todos/details.html')
	context = RequestContext(request, {'list': list})
	return HttpResponse(template.render(context))

def complete(request, list_id):
	list = get_object_or_404(List, pk=list_id)

	try:
		request.POST['item']
	except (KeyError, Item.DoesNotExist):
		return render(request, 'list/detail.html', {
            'list': list,
            'error_message': "You didn't select an item.",
        })
	else:
		for item_id in request.POST['item']:
			item = list.item_set.get(pk=item_id)
			item.completed = True
			item.save()
			print(item.completed)

		return HttpResponseRedirect(reverse('todos:detail', args=(list.id,)))

def add_item(request, list_id):
	list = get_object_or_404(List, pk=list_id)
	
