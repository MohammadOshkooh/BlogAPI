from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet

router = SimpleRouter()

router.register('posts', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
