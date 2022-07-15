from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import json, requests
def response_handler(message="",code=200,data={},error_message="",extra={}):
	return Response({"message":message, "code":code, 'data':data,'error_message':error_message,'extra':extra})

def serialiser_errors(serializer):
	error_message = " & ".join([str(serializer.errors.get(error)[0]) for error in serializer.errors])
	return error_message