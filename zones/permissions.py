from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View

from events.models import Event


class SuperUserAuth(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.event.user == request.user
