from rest_framework import generics
from .permissions import SuperUserAuth, IsOwner
from zones.models import Zone
from zones.serializers import ZoneSerializer


class ZoneView(generics.ListCreateAPIView):
    permission_classes = [SuperUserAuth | IsOwner]

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserAuth | IsOwner]

    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

    lookup_url_kwarg = "zone_id"
