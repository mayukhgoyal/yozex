from dataclasses import fields
from modules.posts.models import *
from rest_framework import serializers
import pdb, re

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = "__all__"