# users/urls.py
from django.urls import include, path
from Users.views import dashboard, register

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
]
