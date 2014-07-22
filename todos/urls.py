from django.conf.urls import patterns, include, url

from todos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<list_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<list_id>\d+)/complete/$', views.complete, name='complete'),
    url(r'^(?P<list_id>\d+)/add-item/$', views.add_item, name='add_item'),
)