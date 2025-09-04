from .models import Comment, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

