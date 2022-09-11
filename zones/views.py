from rest_framework import generics

from zones.models import Zone
from zones.permissions import (IsOwner, IsSuperuser,
                               IsSuperuserOrAuthenticatedToCreate, IsUser)
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
  permission_classes = [IsSuperuserOrAuthenticatedToCreate]
  
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveAPIView):
  permission_classes = [IsSuperuser | IsUser]

  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"


class ZoneDetailView(generics.UpdateAPIView):
  permission_classes = [IsSuperuser | IsOwner]

  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"

class ZoneDetailView(generics.DestroyAPIView):
  permission_classes = [IsSuperuser | IsOwner]

  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"
