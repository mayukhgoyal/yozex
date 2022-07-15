from email import message
from rest_framework import generics
from modules.feedbacks.models import *
from api.v1.modules.serializers.mobile.feedback_serializer import *
from api.v1.modules.response_handler import response_handler
import pdb

class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbackSerializer
    def create(self, request,*args, **kwargs):
        queryset = super().create(request, *args, **kwargs)
        message = "Customer Family create successfully"
        return response_handler(message=message, data=queryset.data)
