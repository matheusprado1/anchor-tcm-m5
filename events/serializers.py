from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = "__all__"
    read_only_fields = ["created_at", "user", "address"]

class EventDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ["name", "description", "duration", "date", "full_age", "created_at", "updated_at", "is_active"]
    read_only_fields = ["created_at", "user_id", "address_id"]