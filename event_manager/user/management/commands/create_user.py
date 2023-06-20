from django.core.management.base import BaseCommand, CommandParser
from django.utils.translation import gettext_lazy as _
from user.factories import UserFactory
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        """
        Add Arguments to subcommand
        python manage.py create_user -n 10
        """
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help=_("Anzahl der USer, die generiert werden sollen"),
            required=True,
        )
        parser.epilog = "Nutzungshinweis: python manage.py create_user -n 20"
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        number = kwargs.get("number", 1)
        get_user_model().objects.exclude(username="admin").delete()
        for i in range(number):
            user = UserFactory()
            print(f"{user} wurde angelegt")
