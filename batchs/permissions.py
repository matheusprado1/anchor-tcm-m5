from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, View


# class IsOwner(BasePermission):

# não consegui fazer a permissão funcionar.

#     def has_permission(self, request: Request, view: View) -> bool:
#         return request.user and request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj == request.user


class IsSuperuser(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )
