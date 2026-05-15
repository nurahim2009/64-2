from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CategoryForm, PostForm

# 1. ГЛАВНАЯ СТРАНИЦА (то, что вызывало ошибку)
def home(request):
    # Фильтруем: опубликовано и рейтинг > 5
    posts = Post.objects.filter(is_published=True, rate__gt=5).order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})

# 2. ДЕТАЛЬНАЯ СТРАНИЦА ПОСТА
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

# 3. СОЗДАНИЕ КАТЕГОРИИ
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'posts/create_category.html', {'form': form})

# 4. СОЗДАНИЕ ПОСТА
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})