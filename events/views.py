from rest_framework import generics
from .models import Event
from addresses.models import Address
from .serializers import EventSerializer, EventDetailSerializer, EventDistanceSerializer
from .mixins import SerializerByMethodMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ListCreateEventView(SerializerByMethodMixin, generics.ListCreateAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  serializer_map = {"GET": EventSerializer, "POST": EventSerializer}
  queryset = Event.objects.all()

  lookup_url_kwarg = "event_id"


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Event.objects.all()
  serializer_class = EventDetailSerializer

  lookup_url_kwarg = "event_id"

class EventDistanceView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # ajustar aqui

    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer
