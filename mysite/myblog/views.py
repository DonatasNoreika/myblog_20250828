from django.shortcuts import render, reverse
from django.views import generic
from .models import Post, Comment, CustomUser
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm, CustomUserChangeForm, CustomUserCreateForm
from django.urls import reverse_lazy


def search(request):
    query = request.GET.get('query')
    post_search_results = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query))
    context = {
        'query': query,
        'posts': post_search_results,
    }
    return render(request, template_name="search.html", context=context)


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


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post", kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.get_object()
        form.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content', 'cover']
    success_url = reverse_lazy("userposts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

