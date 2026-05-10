from django.shortcuts import render, get_object_or_404
from .models import Post

# Главная страница
def home(request):
    posts = Post.objects.filter(is_published=True, rate__gt=5).order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})

# ВОТ ЭТА ФУНКЦИЯ ДОЛЖНА БЫТЬ ЗДЕСЬ:
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})