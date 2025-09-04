from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

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


class UserPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "user_posts.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class UserCommentListView(LoginRequiredMixin, generic.ListView):
    model = Comment
    template_name = 'user_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)