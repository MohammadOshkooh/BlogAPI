from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, CommentViewSet

router = SimpleRouter()

router.register('posts', ArticleViewSet, basename='articles')

comment_router = SimpleRouter()
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls))
]

