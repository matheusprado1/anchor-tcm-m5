from events.models import Event
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View


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
    event = Event.objects.get(id=request.data["event"])
    return event.user == request.user
