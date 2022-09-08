from rest_framework import generics

from .models import Event
from .serializers import EventSerializer, EventDetailSerializer


class EventView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventDetailView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer