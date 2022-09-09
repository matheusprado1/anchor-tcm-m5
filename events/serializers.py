from rest_framework import serializers
from addresses.serializers import AddressSerializer
from .models import Event


class EventSerializer(serializers.ModelSerializer):
  # address = AddressSerializer()

  class Meta:
    model = Event
    fields = "__all__"
    read_only_fields = ["created_at", "user", "address"]

class EventDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ["name", "description", "duration", "date", "full_age", "is_active"]
    read_only_fields = ["created_at", "user_id", "address_id"]

  # address = AddressSerializer(read_only=True)
