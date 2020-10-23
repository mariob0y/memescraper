from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .models import Post
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
