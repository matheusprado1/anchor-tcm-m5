from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View


class IsSuperuserOrIsOwner(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method != "GET":

            return request.user.is_superuser or request.user.is_staff

        return True
