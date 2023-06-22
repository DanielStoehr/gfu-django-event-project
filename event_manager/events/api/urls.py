from django.urls import path

from . import views

event_urlpatterns = [
    path("", views.EventListAPIView.as_view(), name="events_list_create")
]

category_urlpatterns = [
    path(
        "categories/",
        views.CategoryListAPIView.as_view(),
        name="categories_list_create",
    ),
]

urlpatterns = [*event_urlpatterns, *category_urlpatterns]
