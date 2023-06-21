from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.ListUserView.as_view(), name="users"),
    path("token", obtain_auth_token, name="user_token"),
]
