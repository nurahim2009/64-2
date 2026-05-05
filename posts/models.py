from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)       # Заголовок
    content = models.TextField()                    # Текст поста
    rate = models.IntegerField(default=0)           # Оценка/рейтинг
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    updated_at = models.DateTimeField(auto_now=True)     # Дата изменения

    def __str__(self):
        return self.title