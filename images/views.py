from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Image
from .serializers import ImageSerializer


# Talitta esteve aqui, modifiquei o nome do ImageView para EventImageView.
class EventImageView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "event_id"


# Talitta esteve aqui, adicionei a view de user foto.
class UserImageView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    lookup_url_kwarg = "user_id"


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
