import random
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from events.factories import EventFactory
from events.factories import CategoryFactory
from django.contrib.auth import get_user_model
from events.models import Category, Event


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

        for model in [Event, Category]:
            model.objects.all().delete()

        categories = CategoryFactory.create_batch(number_categories)
        users = get_user_model().objects.all()

        if not users:
            raise SystemExit("Es müssen User existieren, um Events zu generieren")

        for event in range(number_events):
            e = EventFactory(
                category=random.choice(categories), author=random.choice(users)
            )

            e.full_clean()
