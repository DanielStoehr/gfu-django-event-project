from unicodedata import category

from django.db import models
from django.db.models.query import QuerySet


class EventQuerySet(models.QuerySet):
    """
    Event.objects.active().sports()
    """

    def active(self) -> models.QuerySet:
        return self.filter(is_active=True)

    def sports(self) -> models.QuerySet:
        return self.filter(category__name="Sports")


class EnhancedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return EventQuerySet(self.model, using=self._db).select_related(
            "category", "author"
        )


class ActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_active=True)


class CategoryManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().annotate(number_of_events=models.Count("events"))
