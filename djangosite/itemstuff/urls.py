from django.conf.urls import patterns, url
from itemstuff import views

urlpatterns = patterns('',
	url(r'^createItem/$', views.createItem, name='createItem'),
	url(r'^editItem/$', views.editItem, name='editItem'),
)
