from geopy import distance
from geopy.geocoders import Nominatim
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "photo, name, description, duration, date, full_age, created_at,"
            " is_active"
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


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
