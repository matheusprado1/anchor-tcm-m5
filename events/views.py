from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status


from .mixins import SerializerByMethod
from .models import Event
from .serializers import (EventDetailSerializer, EventDistanceSerializer,
                          EventSerializer)


class EventView(SerializerByMethod, generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_map = {"GET": EventSerializer, "POST": EventDetailSerializer}


class EventDetailView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


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
