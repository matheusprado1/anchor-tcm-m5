from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticatedOrReadOnly
=======

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

>>>>>>> d28e29aac41329ad57916f9e4b0fdc4398b33f29

from zones.models import Zone
from zones.serializers import ZoneSerializer

from .permissions import IsOwner, SuperUserAuth


class ZoneView(generics.ListCreateAPIView):
<<<<<<< HEAD
    permission_classes = [IsOwner | SuperUserAuth]
=======
   
    permission_classes = [IsAuthenticatedOrReadOnly]
>>>>>>> d28e29aac41329ad57916f9e4b0fdc4398b33f29

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
<<<<<<< HEAD
    permission_classes = [IsOwner | SuperUserAuth]
=======

    permission_classes = [IsAuthenticatedOrReadOnly]

>>>>>>> d28e29aac41329ad57916f9e4b0fdc4398b33f29

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

    lookup_url_kwarg = "id"
