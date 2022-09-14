from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from zones.models import Zone
from zones.serializers import ZoneSerializer

from .permissions import IsOwner, SuperUserAuth


class ZoneView(generics.ListCreateAPIView):

    permission_classes = [IsOwner | SuperUserAuth]


    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner | SuperUserAuth]

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

    lookup_url_kwarg = "id"
