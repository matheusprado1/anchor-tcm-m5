from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ["photo, name, description, duration, date, full_age, created_at, is_active"]


class EventDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = "__all__"