from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),         # homepage: /
    path("health/", views.health, name="health")  # health check: /health/
]

