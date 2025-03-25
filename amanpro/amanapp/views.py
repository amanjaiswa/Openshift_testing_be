from django.shortcuts import render
from django.middleware import http
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import logging

logger=logging.getLogger(__name__)



# Create your views here.



class NewRequestView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            print(request.data)
            logging.info(f"data recieved is {request.data}")
            return Response({"message":" request successful"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

