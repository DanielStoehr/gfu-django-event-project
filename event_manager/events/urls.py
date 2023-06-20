from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import (
    EventCreateView,
    EventDeleteView,
    EventDetailView,
    EventListView,
    EventUpdateView,
)

app_name = "events"

urlpatterns = [
    path("", EventListView.as_view(), name="events"),
    path("<int:pk>", EventDetailView.as_view(), name="event_detail"),
    path("create", EventCreateView.as_view(), name="event_create"),
    path("update/<int:pk>", EventUpdateView.as_view(), name="event_update"),
    path("delete/<int:pk>", EventDeleteView.as_view(), name="event_delete"),
]
