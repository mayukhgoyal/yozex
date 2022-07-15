from email import message
from rest_framework import generics
from modules.posts.models import *
from api.v1.modules.serializers.mobile.post_serializer import *
from api.v1.modules.response_handler import response_handler
import pdb

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def list(self, request):
        query_set = self.queryset
        serializers = self.serializer_class(query_set, many=True)
        message = "Post list fetched successfully"
        return response_handler(message=message, data=serializers.data)