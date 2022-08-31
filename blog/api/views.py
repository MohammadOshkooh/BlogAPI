from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrIsAdmin

from .serializers import ArticleSerializers, CommentSerializers
from blog import models


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializers

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'delete']:
            permission_classes = [IsOwnerOrIsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
