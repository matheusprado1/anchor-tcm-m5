from django.shortcuts import render
from rest_framework import generics

from addresses.models import Address
from addresses.serializers import AddressSerializer

# Create your views here.


class AddressesView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save()
