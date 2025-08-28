from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q

def search(request):
    query = request.GET.get('query')
    post_search_results = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query))
    context = {
        'query': query,
        'posts': post_search_results,
    }
    return render(request, template_name="search.html", context=context)

class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

