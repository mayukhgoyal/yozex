from email import message
from rest_framework import generics
from modules.categories.models import *
from api.v1.modules.serializers.mobile.category_serializer import *
from api.v1.modules.response_handler import response_handler
import pdb
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request):
        query_set = self.queryset
        serializers = self.serializer_class(query_set, many=True)
        message = "Category list fetched successfully"
        return response_handler(message=message, data=serializers.data)


class CategoryDeleteAPIView(generics.DestroyAPIView):
	queryset = Category.objects.all()
	serializer_class =  CategorySerializer
	def delete(self, request, pk):
		query_obj = self.get_object()        
		query_obj.delete()
		message = 'Customer Family member deleted successfully'
		return response_handler(message=message)