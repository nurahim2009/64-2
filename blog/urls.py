from django.urls import path, include # Добавь include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Это добавит login/logout автоматически
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    # ... остальные пути
]