from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """
    Article model
    """
    title = models.CharField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comment model
    """
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.owner.username
