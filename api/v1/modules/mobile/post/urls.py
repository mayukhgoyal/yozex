from django.urls import path, re_path
from .post_controller import *
urlpatterns = [
    path('list',PostListAPIView.as_view(), name="post-list")
]