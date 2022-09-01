from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated


class IsArticleOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(IsAdminUser or
                    IsAuthenticated and bool(obj.author == request.user))


class IsOwnerOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(IsAdminUser or
                    IsAuthenticated and bool(obj.owner == request.user))
