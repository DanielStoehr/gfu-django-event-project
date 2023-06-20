from typing import Any

from django.forms import ValidationError
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


def datetime_in_future(current_field_value) -> None:
    """Prüft, ob Datum in der Vergangenheit, Falls ja, löse Validationerror aus."""
    if current_field_value <= timezone.now():
        raise ValidationError(_("Datum darf nicht in der Vergangenheit liegen"))


@deconstructible
class BadWordFilter:
    """
    deconstructible => damit der Validator für die Migration serialisiert werden kann
    """

    def __init__(self, word_list: list) -> None:
        self.word_list = word_list

    def __call__(self, current_field_value) -> Any:
        for bad_word in self.word_list:
            if bad_word in current_field_value:
                raise ValidationError(_("Du hast ein böses Wort benutzt:") + bad_word)
