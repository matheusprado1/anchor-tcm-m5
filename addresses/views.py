from rest_framework import generics

from addresses.models import Address
from addresses.permissions import SuperUserAuth
from addresses.serializers import AddressSerializer


class AddressesView(generics.ListCreateAPIView):
    permission_classes = [SuperUserAuth]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserAuth]
    lookup_url_kwarg = "address_id"
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
