from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
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
            "updated_at",
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
            "birthdate": {"required": False},
        }

    read_only_fields = [
        "is_superuser",
        "created_at",
        "updated_at",
        "is_active",
    ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
