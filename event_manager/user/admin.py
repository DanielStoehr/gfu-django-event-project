from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from .models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# admin.site.unregister(User)


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]


admin.site.register(User, UserAdmin)
