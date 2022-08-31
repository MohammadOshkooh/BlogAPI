from rest_framework import serializers
from blog import models


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
