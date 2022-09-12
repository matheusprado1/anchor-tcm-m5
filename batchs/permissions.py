from rest_framework import permissions
from rest_framework.views import Request, View

from batchs.models import Batch


class SuperUserAuth(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


