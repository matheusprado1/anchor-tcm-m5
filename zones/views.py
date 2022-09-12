from rest_framework import generics

from zones.models import Zone
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"
