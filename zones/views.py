from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from zones.models import Zone
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

    lookup_url_kwarg = "zone_id"
