from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser


class IsProfileOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(IsAdminUser or bool(IsAdminUser and obj.id == request.user.id))
