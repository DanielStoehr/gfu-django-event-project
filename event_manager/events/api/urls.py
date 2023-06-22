from django.urls import path

from . import views

event_urlpatterns = []

category_urlpatterns = [
    path(
        "categories/",
        views.CategoryListAPIView.as_view(),
        name="categories_list_create",
    ),
]

urlpatterns = [*event_urlpatterns, *category_urlpatterns]
