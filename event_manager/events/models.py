from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from events.managers import (
    ActiveManager,
    CategoryManager,
    EnhancedManager,
    EventQuerySet,
)
from events.validators import BadWordFilter, datetime_in_future

# Create your models here.
User = get_user_model()


class DateTimeMixin(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateTimeMixin):
    """
    Stores a single Category.
    """

    name = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(
        blank=True, null=True, help_text=_("Eine Beschreibung für die Kategorie")
    )
    objects = CategoryManager()

    @property
    def number_events(self):
        """count number of events"""
        return self.events.count()

    class Meta:
        ordering = ["name"]
        verbose_name = _("Kategorie")
        verbose_name_plural = _("Kategorien")

    def __str__(self):
        return self.name


class Event(DateTimeMixin):
    """
    Stores a single event
    related to :model:`events.Category` and :model:`user.User`
    """

    class GroupSize(models.IntegerChoices):
        SMALL = 5, _("kleine Gruppe")
        MEDIUM = 10, _("Mittelgroße Gruppe")
        BIG = 15, _("Große Gruppe")

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Name"),
        validators=[MinLengthValidator(3)],
    )
    slug = models.SlugField(unique=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Eine Beschreibung für ein Event"),
        verbose_name="Beschreibung",
        validators=[BadWordFilter(["evil"])],
    )
    date = models.DateTimeField(validators=[datetime_in_future])
    is_active = models.BooleanField(default=True)
    min_group = models.IntegerField(choices=GroupSize.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    # objects = models.Manager()  # 1. Manager ist der defaulut Manager
    objects = EnhancedManager().from_queryset(EventQuerySet)()
    # active_objects = ActiveManager()

    class Meta:
        ordering = ["name"]
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:event_detail", args=(self.pk,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    @property
    def related_events(self):
        """
        Ähnliche Events zu einem Event
        gleiche Gruppe, gleiche Mindestgröße
        """
        related_events = Event.objects.filter(
            category=self.category, min_group=self.min_group
        )
        return related_events.exclude(pk=self.pk)[:10]


class Review(DateTimeMixin):
    class Rating(models.IntegerChoices):
        BAD = 1
        GOOD = 2
        AWESOME = 3

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField(
        blank=True,
        null=True,
    )
    rating = models.PositiveIntegerField(choices=Rating.choices)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self) -> str:
        return f"{self.author} / {self.event}"
