from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import CategoryForm, PostForm

# Создание категории
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'posts/create_category.html', {'form': form})

# Создание поста
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})