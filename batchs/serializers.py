from rest_framework import serializers

from .models import Batch


class BatchSerializer(serializers.ModelSerializer):

    number_batch = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
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
        ]

    def get_number_batch(self, obj):
        return


class BatchDetailSerializer(serializers.ModelSerializer):

    number_batch = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = [
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
