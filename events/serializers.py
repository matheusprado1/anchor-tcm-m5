from addresses.models import Address
from addresses.serializers import AddressSerializer
from geopy import distance
from geopy.geocoders import Nominatim
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "duration",
            "date",
            "classification",
            "created_at",
            "is_active",
            "address",
        ]
        read_only_fields = ["created_at"]

        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Event.objects.all(),
                        message="This username already exists",
                    )
                ]
            }
        }

    def create(self, validated_data):
        address_serializer = AddressSerializer(
            data=validated_data.pop("address")
        )
        address_serializer.is_valid(raise_exception=True)

        validated_address = address_serializer.save()

        return Event.objects.create(
            **validated_data, address=validated_address
        )


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["created_at", "user_id", "address_id"]


class EventDistanceSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_distance(self, obj):
        user_address = self.context["request"].user.address

        try:
            if obj.address.latitude is None or obj.address.latitude is None:
                raise AttributeError
            return round(
                distance.distance(
                    (user_address.latitude, user_address.longitude),
                    (obj.address.latitude, obj.address.longitude),
                ).km,
                2,
            )
        except AttributeError:
            return "User or event invalid address for distance"
