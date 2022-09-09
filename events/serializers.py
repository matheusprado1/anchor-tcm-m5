from geopy import distance
from geopy.geocoders import Nominatim
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

class EventDistanceSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_distance(self, obj):
        geolocator = Nominatim(user_agent="address")
        user_address = self.context["request"].user.address.get_full_address()
        user_location = geolocator.geocode(user_address)
        event_address = obj.address.get_full_address()
        event_location = geolocator.geocode(event_address)

        try:
            return distance.distance(
                (user_location.latitude, user_location.longitude),
                (event_location.latitude, event_location.longitude),
            ).km
        except AttributeError:
            return "User or event invalid address for"
