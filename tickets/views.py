from rest_framework import generics
from django.shortcuts import get_object_or_404
from batchs.models import Batch

from tickets.permissions import IsSuperuser, IsUser, IsOwner, IsSuperuserOrAuthenticatedToCreate, IsUser
from tickets.models import Ticket
from tickets.serializers import TicketSerializer

class TicketView(generics.ListCreateAPIView):

    permission_classes = [IsSuperuserOrAuthenticatedToCreate]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        
        get_object_or_404(Batch, pk=serializer.validated_data["batch_id"])
        serializer.save()


class UserTicketsView(generics.ListAPIView):
    
    permission_classes = [IsSuperuser | IsUser]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs["user_id"])

class TicketDeleteView(generics.DestroyAPIView):

    lookup_url_kwarg = "ticket_id"
    permission_classes = [IsSuperuser | IsOwner]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer