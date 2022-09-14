from geopy import distance
from geopy.geocoders import Nominatim
from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        read_only_fields = ["latitude", "longitude"]

    def create(self, data):
        geolocator = Nominatim(user_agent="address")
        search_address = (
            f"{data['street']}, {data['number']}. {data['city']},"
            f" {data['zipcode']}"
        )
        location = geolocator.geocode(search_address)
        latitude = location.latitude if location else None
        longitude = location.longitude if location else None

        return Address.objects.create(
            **data, latitude=latitude, longitude=longitude
        )
