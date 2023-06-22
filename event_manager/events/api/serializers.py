from django.utils import timezone
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


class ReviewInlineSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Review
        fields = ("rating", "review", "author")


class EventOutputSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    reviews = ReviewInlineSerializer(many=True)
    days_to_event = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = (
            "id",
            "name",
            "sub_title",
            "category",
            "date",
            "min_group",
            "author",
            "min_group",
            "reviews",
            "days_to_event",
        )

    def get_days_to_event(self, object):
        diff = object.date - timezone.now()
        return diff.days


class EventInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ("name", "sub_title", "category", "date", "min_group")
