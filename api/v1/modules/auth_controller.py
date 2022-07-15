from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from api.v1.modules.serializers.mobile.user_serializer import *
from api.v1.modules.response_handler import response_handler, serialiser_errors
from modules.users.models import User, UserOtp
import random, pdb

class Login(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		#pdb.set_trace()
		mobile = request.data.get('mobile',None)
		if mobile:
			users = User.objects.filter(mobile__iexact=mobile)
			if users.exists():				
				return response_handler(message='Please check your mobile for activation code.')
			else:
				message = "User not found"
				return response_handler(message,error_message=message,code=500)
		else:
			message = "Invalid mobile"
			return response_handler(message,error_message=message,code=500)