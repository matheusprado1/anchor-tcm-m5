from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Image
from .serializers import ImageSerializer


class ImageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "event_id"


class ListImageView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "image_id"
