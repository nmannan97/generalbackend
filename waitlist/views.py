'''
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed
from .models import waitlist
import json
'''
# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
# Create your views here.
  
class waitlistView(APIView):
    
    serializer_class = waitlistSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name, "email": detail.email, 'phonenumber': detail.phonenumber, 'postion': detail.position} 
        for detail in waitlist.objects.all()]
        return Response(detail)
  
    def post(self, request):
        serializer = waitlistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)