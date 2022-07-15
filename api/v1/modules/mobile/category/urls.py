from django.urls import path, re_path
from .category_controller import *
urlpatterns = [
    path('list',CategoryListAPIView.as_view(), name="category-list")
]