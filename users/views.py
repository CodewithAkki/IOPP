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
# Create your views here.

class CreateUser (generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    def post(self, request,format = None):
        print(request.data)
        user = UserSerializer(data = request.data)
        if user.is_valid():
            user.save()
            current_user = user.objects.get(email=request.data['email'])
            current_user.set_password(request.data['password'])
            current_user.is_active=True
            current_user.save()
            user = UserSerializer(current_user)
            return Response({"message":"user registered sccessfully",'userData':user.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":"fail to register",'userData':user.data,"status ": status.HTTP_400_BAD_REQUEST})  
    def get(self, request,format = None): 
            user_data = user.objects.all()
            print(user_data)
            return Response({"status ": status.HTTP_201_CREATED})
           
  
class UpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
        queryset = user.objects.all()
        serializer_class = UserSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['=email']

        