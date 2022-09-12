from addresses.models import Address
from addresses.serializers import AddressSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "photo",
            "email",
            "cpf",
            "birthdate",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "is_superuser",
            "created_at",
            "address",
        ]

        extra_kwargs = {
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This username already exists",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This email address already exists",
                    )
                ]
            },
            "cpf": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This cpf number already exists",
                    )
                ]
            },
            "password": {"write_only": True},
            "is_staff": {"required": True},
        }

    read_only_fields = ["is_superuser", "created_at", "is_active"]

    def create(self, validated_data):
        validated_address, _ = Address.objects.get_or_create(
            **validated_data.pop("address")
        )
        return User.objects.create_user(
            **validated_data, address=validated_address
        )

    def update(self, instance, validated_data):
        if validated_data.get("address"):
            address_poped = validated_data.pop("address")

            verificated_address, _ = Address.objects.get_or_create(
                **address_poped
            )
            instance.address = verificated_address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "photo",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "cpf",
            "email",
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
