from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, Request, Response, status

from events.filters import DistanceFilter

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
    queryset = Event.objects.all()
    serializer_class = EventDistanceSerializer


class EventDistanceLteView(generics.ListAPIView):
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


# class EventDistanceLteView(APIView, PageNumberPagination):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request: Request, dist: int) -> Response:
#         events = Event.objects.all()
#         import ipdb

#         # result_page = self.paginate_queryset(events, request, view=self)

#         serializer = EventDistanceSerializer(events, many=True)
#         ipdb.set_trace()

#         filtered_serializer = [
#             event for event in serializer.data if event["distance"] < dist
#         ]

#         return Response("(filtered_serializer)")


class EventDistanceGteView(APIView, PageNumberPagination):
    def get(self, request: Request, dist: int) -> Response:
        events = Event.objects.all()
        result_page = self.paginate_queryset(events, request, view=self)

        serializer = EventDistanceSerializer(result_page, many=True)

        filtered_serializer = [
            event for event in serializer.data if event["distance"] > dist
        ]

        return self.get_paginated_response(filtered_serializer)


# class EventDistanceView(generics.ListAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]  # ajustar aqui
#     queryset = Event.objects.all()
#     serializer_class = EventDistanceSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = DistanceFilter

# def list(self, request, *args, **kwargs):
#     import ipdb

#     ipdb.set_trace()

#     queryset = self.filter_queryset(self.get_queryset())

#     page = self.paginate_queryset(queryset)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)

#     serializer = self.get_serializer(queryset, many=True)

#     return Response(serializer.data)
