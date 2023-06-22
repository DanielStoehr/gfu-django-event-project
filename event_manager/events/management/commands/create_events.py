import random
from typing import Final

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from events.factories import CategoryFactory, EventFactory, ReviewFactory
from events.models import Category, Event, Review

MAX_TAGS: Final = 6


class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        """Add Arguments to our subcommand.
        python manage.py create_events -e 10 -c 3
        """
        parser.add_argument(
            "-e",
            "--events",
            type=int,
            help=_("Anzahl der Events, die generiert werden sollen"),
            required=True,
        )

        parser.add_argument(
            "-c",
            "--categories",
            type=int,
            help=_("Anzahl der Kategorien, die generiert werden sollen"),
            required=True,
        )

        parser.epilog = "Nutzungshinweis: python manage.py create_events -e 10 -c 3"

    def handle(self, *args, **kwargs):
        number_events = kwargs.get("events", 10)
        number_categories = kwargs.get("categories", 10)

        for model in [Event, Category, Review]:
            model.objects.all().delete()

        categories = CategoryFactory.create_batch(number_categories)
        users = get_user_model().objects.all()

        if not users:
            raise SystemExit("Es müssen User existieren, um Events zu generieren")

        for event in range(number_events):
            event = EventFactory(
                category=random.choice(categories), author=random.choice(users)
            )

            # event.full_clean() # löst ValidationError aus
            for n in range(random.randint(0, MAX_TAGS)):
                ReviewFactory(event=event, author=random.choice(users))
