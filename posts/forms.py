from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'category', 'tags', 'is_published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), # Позволяет выбирать галочками
        }