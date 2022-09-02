from django.urls import path, include
from .views import UserViewSet, UserPostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')

user_post_router = SimpleRouter()

user_post_router.register('posts', UserPostViewSet, basename='user_posts')

urlpatterns = [
    path('users/<user_id>/', include(user_post_router.urls)),
    path('', include(router.urls)),
]
