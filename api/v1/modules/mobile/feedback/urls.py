from django.urls import path, re_path
from .feedback_controller import *

urlpatterns = [
     path('create',FeedbackCreateAPIView.as_view(), name="feedback-create")
]