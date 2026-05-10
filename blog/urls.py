urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/add/', views.create_category, name='create_category'), # Ссылка для категории
    path('post/add/', views.create_post, name='create_post'),             # Ссылка для поста
]