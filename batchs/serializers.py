from rest_framework import serializers

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):
    total_sold_tickets = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
            "id",
            "number_batch",
            "price",
            "quantity",
            "due_date",
            "is_active",
            "created_at",
            "zone",
            "total_sold_tickets",
        ]
        read_only_fields = [
            "created_at",
            "id",
            "number_batch",
        ]

    def get_total_sold_tickets(self, obj):
        return obj.get_sold_tickets()


class BatchDetailSerializer(serializers.ModelSerializer):
    total_sold_tickets = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
            "id",
            "number_batch",
            "price",
            "quantity",
            "due_date",
            "is_active",
            "created_at",
            "zone",
            "total_sold_tickets",
        ]
        read_only_fields = ["created_at", "number_batch", "total_sold_tickets"]

    def get_total_sold_tickets(self, obj):
        return obj.get_sold_tickets()
