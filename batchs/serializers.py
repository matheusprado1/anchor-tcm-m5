from rest_framework import serializers

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):

    number_batch = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
            "batch_id",
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
        ]

    def create(self, validated_data):
        validated_zone, _ = Batch.objects.get_or_create(
            **validated_data.pop("zone")
        )

        return Batch.objects.create(
            **validated_data, zone=validated_zone
        )

    def get_number_batch(self, obj):
        return


class BatchDetailSerializer(serializers.ModelSerializer):

    number_batch = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
            "batch_id",
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

    def get_number_batch(self, obj):
        return
