from django.contrib.auth import views as auth_views
from django.urls import include, path

app_name = "user"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    )
]
