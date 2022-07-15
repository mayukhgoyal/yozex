from rest_framework import serializers
from modules.users.models import *
from rest_framework.authtoken.models import Token
import pdb, re


class UserLoginSerializer(serializers.Serializer):
	mobile = serializers.CharField(max_length=200, required=True)
	def validate(self, attrs):
		users = User.objects.filter(mobile__iexact=atts.get('email'))
		if not users.exists():
			raise serializers.ValidationError("Mobile Number not found.")

		return attrs