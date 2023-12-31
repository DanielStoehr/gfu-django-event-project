from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model."""

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "email", "date_joined")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            "date_joined": {"read_only": True},
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
