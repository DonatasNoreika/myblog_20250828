from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Comment(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.date_created} ({self.post.title})"

    class Meta:
        ordering = ['-date_created']
