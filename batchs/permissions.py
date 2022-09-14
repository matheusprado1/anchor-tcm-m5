from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View
from zones.models import Zone
from django.shortcuts import get_object_or_404


from batchs.models import Batch


class SuperUserAuth(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        zone = get_object_or_404(Zone,id=request.data["zone"])
        return zone.event.user == request.user
