from .models import Comment, CustomUser
from django import forms

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

