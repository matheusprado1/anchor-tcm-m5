from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

class ImageView(generics.CreateAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Image.objects.all()
  serializer_class = ImageSerializer

  lookup_url_kwarg = "event_id"


class ListImageView(generics.ListAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Image.objects.all()
  serializer_class = ImageSerializer


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]

  queryset = Image.objects.all()
  serializer_class = ImageSerializer

  lookup_url_kwarg = "image_id"