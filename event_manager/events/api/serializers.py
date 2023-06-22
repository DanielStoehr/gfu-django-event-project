from events import models
from rest_framework import serializers


class CategoryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
