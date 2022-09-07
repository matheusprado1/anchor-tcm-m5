from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User


class IsUserOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(
        self,
        request: Request,
        view: View,
        user: User,
    ) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return user.is_staff == request.user.id or request.user.is_superuser
