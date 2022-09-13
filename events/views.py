from rest_framework import generics
from .models import Event
from addresses.models import Address
from .serializers import EventSerializer, EventDetailSerializer, EventDistanceSerializer
from .mixins import SerializerByMethodMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsSuperuser, IsUser, IsOwner, IsSuperuserOrAuthenticatedToCreate, IsUser
from rest_framework.views import APIView, Request, Response, status

from .mixins import SerializerByMethodMixin
from .models import Event
from .serializers import (EventDetailSerializer, EventDistanceSerializer,
                          EventSerializer)

class ListCreateEventView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrAuthenticatedToCreate]

    serializer_map = {"GET": EventSerializer, "POST": EventSerializer}
    queryset = Event.objects.all()

    lookup_url_kwarg = "event_id"


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuser | IsOwner]

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    lookup_url_kwarg = "event_id"


class EventDistanceView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer


class EventDistanceLteView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        dist = kwargs["dist"]
        filtered_serializer = [
            event for event in serializer.data if event["distance"] < dist
        ]
        return self.get_paginated_response(filtered_serializer)


class EventDistanceGteView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        dist = kwargs["dist"]
        filtered_serializer = [
            event for event in serializer.data if event["distance"] > dist
        ]
        return self.get_paginated_response(filtered_serializer)
