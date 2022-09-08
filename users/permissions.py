from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User


class IsUserAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            return False
        return True


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user == obj
            and request.user.is_authenticated
            or request.user.is_superuser
            and obj.is_superuser is False
            # se ele nao for super user e for objeto dele
            # se ele for superuser e for objecto dele
            # se ele for superuser e o objeto for de um user
        )
