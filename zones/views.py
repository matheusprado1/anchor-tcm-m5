from django.shortcuts import render

from rest_framework import generics

from zones.models import Zone
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
  queryset = Zone.objects.all()
  serializer_class = ZoneSerializer
