from django.urls import path, re_path
from .location_controller import *
urlpatterns = [
    path('list',LocationListAPIView.as_view(), name="location-list")
]