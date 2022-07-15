from dataclasses import fields
from modules.locations.models import Location
from rest_framework import serializers
import pdb, re

class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = "__all__"