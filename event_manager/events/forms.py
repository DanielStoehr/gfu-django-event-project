from xml.dom import ValidationErr

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            )
        }

    def clean_sub_title(self) -> str:
        """
        Bereinige das Feld sub_title
        """
        current_sub_title = self.cleaned_data["sub_title"]
        illegal_starts = ("*", "#")
        if isinstance(current_sub_title, str) and current_sub_title.startswith(
            illegal_starts
        ):
            raise forms.ValidationError(_("Dieses Zeichen ist nicht erlaubt"))

        return current_sub_title

    def clean_date(self):
        current_date = self.cleaned_data["date"]
        return current_date

    def clean(self):
        """generiert self.cleaned_data dictionary"""
        super().clean()

        name = self.cleaned_data["name"]
        sub_title = self.cleaned_data["sub_title"]

        if all([name, sub_title]):
            if name == sub_title:
                raise forms.ValidationError(
                    "name und sub_title darf nicht gleich sein."
                )

        return self.cleaned_data
