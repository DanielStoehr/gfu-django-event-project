from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

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

    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Eine Beschreibung für ein Event"),
        verbose_name="Beschreibung",
    )
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    min_group = models.IntegerField(choices=GroupSize.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    class Meta:
        ordering = ["name"]
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name
