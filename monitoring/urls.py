from django.urls import path

from .views import (
    asin_view,
    switch_system,
    delete_asin,
)

urlpatterns = [
    path("", asin_view, name="home"),
    path("switch-api/<str:pk>", switch_system, name="switch-api"),
    path("delete-asin/<str:pk>", delete_asin, name="delete-asin"),
]
