from dataclasses import fields
from rest_framework import serializers
from modules.categories.models import *
from rest_framework.authtoken.models import Token
import pdb, re

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"