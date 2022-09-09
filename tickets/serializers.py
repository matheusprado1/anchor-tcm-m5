from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ["id", "user_id", "batch_id", "created_at"]


    def create(self, validated_data):

        user = self.context["request"].user
        return Ticket.objects.create(**validated_data, user=user)
