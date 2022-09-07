from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Event
from .serializers import EventDetailSerializer, EventSerializer
from .mixins import SerializerByMethod

class EventView(SerializerByMethod,generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_map = {"GET": EventSerializer, "POST": EventDetailSerializer}


class EventDetailView(generics.RetrieveUpdateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventDetailSerializer
