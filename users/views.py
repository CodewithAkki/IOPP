from django.shortcuts import render
from .models import user
from .serializers import UserSerializer
from rest_framework import generics
from django_genericfilters.views import FilteredListView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status 
import json
# Create your views here.

class CreateUser (generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    def post(self, request,format = None):
        
        user_data = UserSerializer(data = request.data)
        if user_data.is_valid():
            user_data.save()
            current_user = user.objects.get(email=request.data['email'])
            current_user.set_password(request.data['password'])
            current_user.is_active=True
            current_user.save()
            user = UserSerializer(current_user)
            return Response({"message":"user registered sccessfully",'userData':user.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":user_data.errors,'userData':user.data,"status ": status.HTTP_400_BAD_REQUEST})  
    
    def get(self, request,format = None): 
            try:
                user_data = user.objects.all()
                serializer=UserSerializer(user_data,many=True)
                print(serializer.data)
                return Response({"data":serializer.data,"status ": status.HTTP_201_CREATED})
            except user.DoesNotExist:
                return Response({"data":"table not exists","status ": status.HTTP_401_UNAUTHORIZED})
                 
           
  
class UpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
        queryset = user.objects.all()
        serializer_class = UserSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['=email']

        