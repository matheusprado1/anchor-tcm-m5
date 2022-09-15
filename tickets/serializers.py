from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "user", "batch", "created_at"]
        extra_kwargs = {
            # "qnt_tickets": {"write_only": True},
            "user": {"read_only": True},
        }
