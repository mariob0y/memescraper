from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .models import Post


def home(request):
	posts = Post.objects.order_by('date').reverse()
	paginator = Paginator(posts, 18)
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)

	return render(request, "home.html", {'posts': posts})

def random(request):
	posts = Post.objects.order_by('?')
	paginator = Paginator(posts, 18)
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)

	return render(request, "home.html", {'posts': posts})

from django.views.generic.list import ListView

class PostsView(ListView):
    model = Post 
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'posts.html'
    ordering = ['-date']

class RandomView(ListView):
    model = Post 
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'posts.html'
    ordering = ['?']