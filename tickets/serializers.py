from rest_framework import serializers
from rest_framework.serializers import UUIDField
from tickets.models import Ticket
from batchs.models import Batch
from django.shortcuts import get_object_or_404


class TicketSerializer(serializers.ModelSerializer):

    batch_id = UUIDField()
    class Meta:
        model = Ticket
        fields = ["id", "user_id", "batch_id", "created_at"]


    def create(self, validated_data):
        user = self.context["request"].user
        return Ticket.objects.create(**validated_data, user=user)
