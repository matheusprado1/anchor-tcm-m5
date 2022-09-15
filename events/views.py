from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from events.serializers import EventDetailSerializer, EventDistanceSerializer, EventSerializer

from .permissions import IsSuperuserOrIsOwner

from .mixins import SerializerByMethodMixin
from .models import Event


class ListCreateEventView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOrIsOwner]

    serializer_map = {"GET": EventSerializer, "POST": EventSerializer}
    queryset = Event.objects.all()

    lookup_url_kwarg = "event_id"


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserOrIsOwner]

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
        filtered_serializer = [
            event
            for event in serializer.data
            if type(event["distance"]) is not str and event["distance"] >= dist
        ]
        return self.get_paginated_response(filtered_serializer)
