from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path("", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("userposts/", views.UserPostListView.as_view(), name="userposts"),
]