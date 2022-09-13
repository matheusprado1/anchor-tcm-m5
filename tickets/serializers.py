from batchs.models import Batch
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import UUIDField

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "user", "batch", "created_at"]
        extra_kwargs = {
            "qnt_tickets": {"write_only": True},
            "user": {"read_only": True},
        }
