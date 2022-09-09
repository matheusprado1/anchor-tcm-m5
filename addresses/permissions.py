from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from rest_framework.views import Request, View

from addresses.models import Address


class SuperUserAuth(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


class OwnerOrSuperUserAuth(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Address):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # Instance must have an attribute named `owner`.
        import ipdb

        ipdb.set_trace()
        return obj.user == request.user
