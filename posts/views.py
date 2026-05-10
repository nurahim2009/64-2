from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    # Только опубликованные и рейтинг выше 5
    posts = Post.objects.filter(is_published=True, rate__gt=5).order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    # Вьюшка для одного поста
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
