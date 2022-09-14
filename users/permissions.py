from rest_framework import permissions

from users.models import User


class IsUserAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            return False
        return True


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:

        return (
            str(request.user.id) == str(view.kwargs["user_id"])
            and request.user.is_authenticated
            or request.user.is_superuser
            and user.is_superuser is False
        )
