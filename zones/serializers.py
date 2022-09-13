from rest_framework import serializers

from .models import Zone


class ZoneSerializer(serializers.ModelSerializer):
    total_sold_tickets = serializers.SerializerMethodField()

    class Meta:
        model = Zone
        fields = "__all__"
        read_only_fields = ["total_sold_tickets"]

    def get_total_sold_tickets(self, obj):
        return obj.get_sold_tickets()
