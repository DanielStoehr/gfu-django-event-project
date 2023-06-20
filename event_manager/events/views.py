from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import EventForm
from .models import Event

# Create your views here.


class UserIsAuthor(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author


class EventListView(ListView):
    """
    Zeige alle Events
    /events
    """

    model = Event
    context_object_name = "events"
    queryset = Event.objects.select_related("category", "author")


class EventDetailView(DetailView):
    """
    Zeige ein Event
    /events/3
    """

    model = Event
    context_object_name = "event"


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    success_message = _("Event wurde erfolgreich hinzugefügt!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(UserIsAuthor, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    success_message = _("Event wurde erfolgreich geändert!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventDeleteView(UserIsAuthor, SuccessMessageMixin, DeleteView):
    model = Event
    success_message = _("Event wurde erfolgreich gelöscht")
    success_url = reverse_lazy("events:events")
