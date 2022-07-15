from email import message
from rest_framework import generics
from modules.locations.models import *
from api.v1.modules.serializers.mobile.location_serializer import *
from api.v1.modules.response_handler import response_handler
import pdb

class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    def list(self, request):
        query_set = self.queryset
        serializers = self.serializer_class(query_set, many=True)
        message = "Location list fetched successfully"
        return response_handler(message=message, data=serializers.data)