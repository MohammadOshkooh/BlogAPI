from django.contrib.auth import get_user_model
from rest_framework import permissions

from .permissions import IsProfileOwnerOrAdmin
from .seroalizers import UserSerializers
from blog.api.serializers import ArticleSerializers
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = get_user_model().objects.all()

    def get_permissions(self):
        if self.action in ['destroy', 'update']:
            permission_classes = [IsProfileOwnerOrAdmin]
        elif self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class UserPostViewSet(ModelViewSet):
    serializer_class = ArticleSerializers

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['user_id']
        user = get_user_model().objects.filter(id=user_id).first()
        posts = user.posts.all()
        return posts
