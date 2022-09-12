from geopy import distance
from geopy.geocoders import Nominatim
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from addresses.serializers import AddressSerializer

from .models import Event
from addresses.models import Address


class EventSerializer(serializers.ModelSerializer):
  address = AddressSerializer()

  class Meta:
    model = Event
    fields = ["id", "name", "description", "duration", "date", "full_age","created_at", "is_active", "address"]
    read_only_fields = ["created_at"]

    extra_kwargs = {
    "name": {
      "validators": [UniqueValidator(queryset=Event.objects.all(),
        message="This username already exists")]}
    }

  def create(self, validated_data):
    validated_address, _ = Address.objects.get_or_create(
      **validated_data.pop("address")
    )

    return Event.objects.create(
      **validated_data, address=validated_address
    )

  def update(
    self, instance: Event, validated_data):
    if validated_data.get("address"):
      address_dict = validated_data.pop("address")

      verificated_address, _ = Address.objects.get_or_create(
        **address_dict)

      instance.address = verificated_address

    for key, value in validated_data.items():
      setattr(instance, key, value)

    instance.save()
    return instance


class EventDistanceSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_distance(self, obj):
        geolocator = Nominatim(user_agent="address")
        user_address = self.context["request"].user.address.get_full_address()
        event_address = obj.address.get_full_address()
        user_location = geolocator.geocode(user_address)
        event_location = geolocator.geocode(event_address)

        try:
            return distance.distance(
                (user_location.latitude, user_location.longitude),
                (event_location.latitude, event_location.longitude),
            ).km
        except AttributeError:
            return "User or event invalid address for"
