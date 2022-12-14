
from addresses.models import Address
from users.models import User
from addresses.serializers import AddressSerializer

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User



from django.conf import settings
from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
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
            "age",
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

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError(
                "The cpf field must have 11 digits"
            )
        return cpf

    def create(self, validated_data):
        address_serializer = AddressSerializer(
            data=validated_data.pop("address")
        )
        address_serializer.is_valid(raise_exception=True)
        validated_address = address_serializer.save()
        user_mail = User.objects.create_user(
            **validated_data, address=validated_address
        )
        from_email = settings.EMAIL_HOST_USER
        subject = "Welcome to Anchor"
        message = (
            f"Congratulations {user_mail.username}, thank you for registering"
            " in Anchor"
        )
        recipient_list = [
            user_mail.email,
        ]
        send_mail(subject, message, from_email, recipient_list)
        return user_mail

    def get_age(self, obj):
        return obj.age

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

