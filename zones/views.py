from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from zones.models import Zone
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"

class ZoneDetailView(generics.UpdateAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"

class ZoneDetailView(generics.DestroyAPIView):
  serializer_class = ZoneSerializer
  queryset = Zone.objects.all()

  lookup_url_kwarg = "zone_id"
