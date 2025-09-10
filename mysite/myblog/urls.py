from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path("userposts/", views.UserPostListView.as_view(), name="userposts"),
    path("usercomments/", views.UserCommentListView.as_view(), name="usercomments"),
    path("profile/", views.ProfileUpdateView.as_view(), name="profile"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("posts/create", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
]