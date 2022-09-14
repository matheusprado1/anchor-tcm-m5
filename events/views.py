from numbers import Number

from addresses.models import Address
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import APIView, Request, Response, status

from .mixins import SerializerByMethodMixin
from .models import Event
from .permissions import (
    IsOwner,
    IsSuperuser,
    IsSuperuserOrAuthenticatedToCreate,
    IsUser,
)
from .serializers import (
    EventDetailSerializer,
    EventDistanceSerializer,
    EventSerializer,
)


class ListCreateEventView(SerializerByMethodMixin, generics.ListCreateAPIView):

    # "distance": 0.0
    permission_classes = [IsSuperuserOrAuthenticatedToCreate]

    serializer_map = {"GET": EventSerializer, "POST": EventSerializer}
    queryset = Event.objects.all()

    lookup_url_kwarg = "event_id"


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuser | IsOwner]

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    lookup_url_kwarg = "event_id"


class EventDistanceView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer


# VIEW PARA LESS THAN OR EQUAL
class EventDistanceLteView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        dist = kwargs["dist"]
        # IS NOT STR ADC POIS SE NÃO TIVER A LOCALIZAÇÃO, NÃO DEVE SER FILTRADO
        filtered_serializer = [
            event
            for event in serializer.data
            if type(event["distance"]) is not str and event["distance"] <= dist
        ]
        return self.get_paginated_response(filtered_serializer)


# VIEW PARA GREATHER THAN OR EQUAL
class EventDistanceGteView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        dist = kwargs["dist"]
        # IS NOT STR ADC POIS SE NÃO TIVER A LOCALIZAÇÃO, NÃO DEVE SER FILTRADO
        filtered_serializer = [
            event
            for event in serializer.data
            if type(event["distance"]) is not str and event["distance"] >= dist
        ]
        return self.get_paginated_response(filtered_serializer)
