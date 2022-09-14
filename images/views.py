from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Image
from .serializers import ImageSerializer



class EventImageView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "event_id"



class EventListImageView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class EventImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "image_id"


class UserImageView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "user_id"



class UserListImageView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer



class UserImageDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "image_id"
