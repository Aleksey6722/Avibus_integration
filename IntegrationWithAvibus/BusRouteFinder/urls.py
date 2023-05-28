from django.urls import path

from .views import find

urlpatterns = [
    path("findroute/", find),
]