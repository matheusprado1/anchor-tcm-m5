from django_filters import rest_framework as filters
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from events.filters import DistanceFilter

from .mixins import SerializerByMethodMixin
from addresses.models import Address
from .models import Event
from .serializers import (
    EventDetailSerializer,
    EventDistanceSerializer,
    EventSerializer,
)


class ListCreateEventView(SerializerByMethodMixin, generics.ListCreateAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Event.objects.all()
  serializer_map = {"GET": EventSerializer, "POST": EventSerializer}

  def perform_create(self, serializer):
    id_address = self.request.data['address']

    address = Address.objects.get(id = id_address)
    serializer.save(address=address)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Event.objects.all()
  serializer_class = EventSerializer

  lookup_url_kwarg = "event_id"


class EventDistanceView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # ajustar aqui

    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DistanceFilter
