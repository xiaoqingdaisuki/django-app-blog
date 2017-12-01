from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.views.generic import ListView,DetailView
# Create your views here.
def index(request):
	posts = BlogPost.objects.all().order_by('-timestamp')
	return render(request, 'index.html', {'posts':posts})

class Textview(DetailView):
	model = BlogPost
	template_name = 'text.html'