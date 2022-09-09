from django_filters import rest_framework as filters
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from events.filters import DistanceFilter

from .mixins import SerializerByMethodMixin
from .models import Event
from .serializers import (
    EventDetailSerializer,
    EventDistanceSerializer,
    EventSerializer,
)


class EventView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Event.objects.all()
    serializer_map = {"GET": EventSerializer, "POST": EventDetailSerializer}

    def perform_create(self, serializer):
        serializer.save(address=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class EventDistanceView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # ajustar aqui

    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DistanceFilter
