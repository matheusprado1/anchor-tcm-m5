from rest_framework import serializers

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "zone",
        ]


class BatchDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = [
            "id",
            "price",
            "quantity",
            "number_batch",
            "due_date",
            "is_active",
            "zone_id",
            "created_at",
        ]

        read_only_fields = [
            "zone_id",
            "created_at",
        ]
