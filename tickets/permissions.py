from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View


class IsSuperuser(BasePermission):
    def has_permission(self, request: Request, view: View)-> bool:
        return request.user.is_superuser

class IsUser(BasePermission):
    def has_permission(self, request: Request, view: View)-> bool:
        return request.user.id == view.kwargs["user_id"]

class IsSuperuserOrIsOwner(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj)-> bool:
        return request.user.is_superuser or obj.user == request.user

class IsSuperuserOrAuthenticatedToCreate(BasePermission):
    def has_permission(self, request: Request, view: View)-> bool:
        return request.user.is_superuser or (request.method != "GET" and request.user.is_authenticated)
