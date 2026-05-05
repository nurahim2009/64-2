from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail_view(request, post_id):
    # Достаем пост по id, если его нет — выдаем ошибку 404
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'base.html', context={'post': post})
