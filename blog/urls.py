from django.conf.urls import *
from blog.views import index,Textview

app_name = 'blog'

urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^text(?P<pk>[0-9]+)$',Textview.as_view(),name='text'),
	]