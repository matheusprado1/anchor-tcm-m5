from rest_framework import serializers
from zones.serializers import ZoneSerializer

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = [
            "created_at",
            "id",
            "number_batch"
        ]
        depth = 1


class BatchDetailSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = [
            "created_at",
            "number_batch",
        ]
