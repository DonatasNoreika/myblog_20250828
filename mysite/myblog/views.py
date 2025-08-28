from django.shortcuts import render
from django.views import generic
from .models import Post

class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

