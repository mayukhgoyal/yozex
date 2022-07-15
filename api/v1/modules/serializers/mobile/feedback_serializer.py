from dataclasses import fields
from modules.feedbacks.models import *
from rest_framework import serializers
import pdb, re

class FeedbackSerializer(serializers.Serializer):
    class Meta:
        model = Feedbacks
        fields = "__all__"