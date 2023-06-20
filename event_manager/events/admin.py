from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Category, Event
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.


class EventResource(resources.ModelResource):
    class Meta:
        model = Event

    author = fields.Field(
        attribute="author",
        widget=ForeignKeyWidget(get_user_model(), field="username"),
    )


class EventImportAdmin(ImportExportModelAdmin):
    resource_classes = [EventResource]


# admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sub_title",
        "number_events",
    )

    def get_queryset(self, request):
        return Category.objects.prefetch_related("events").all()


@admin.register(Event)
class EventAdmin(EventImportAdmin):
    list_display = (
        "name",
        "sub_title",
        "category",
        "min_group",
        "is_active",
    )
    actions = "make_active", "make_inactive"

    def get_queryset(self, request: HttpRequest):
        """Nur Superuser sehen alle Einträge, andere sehen nur die eigenen"""
        qs = Event.objects.select_related("category", "author").all()
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    @admin.display(description=_("Setzte Events aktiv"))
    def make_active(self, request, queryset):
        """
        queryset = die menge der aktuell ausgewählten Einträge
        """
        queryset.update(is_active=True)

    @admin.display(description=_("Setzte Events inaktiv"))
    def make_inactive(self, request, queryset):
        """
        queryset = die menge der aktuell ausgewählten Einträge
        """
        queryset.update(is_active=False)
