from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from addresses.models import Address
from addresses.permissions import SuperUserAuth
from addresses.serializers import AddressSerializer


class AddressesView(generics.ListCreateAPIView): # ajustar aqui
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserAuth]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressesDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserAuth]  # ajustar aqui
    lookup_url_kwarg = "address_id"
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
