from rest_framework import generics

from tickets.models import Ticket
from tickets.serializers import TicketSerializer

class TicketView(generics.ListCreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketRetrieveView(generics.RetrieveAPIView):

    lookup_url_kwarg = "user_id"
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDeleteView(generics.DestroyAPIView):

    lookup_url_kwarg = "ticket_id"
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer