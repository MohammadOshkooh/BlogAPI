from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']


admin.site.register(Article, ArticleAdmin)
