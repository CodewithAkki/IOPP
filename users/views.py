from django.shortcuts import render
from .models import user,role
from .serializers import UserSerializer
from rest_framework import generics
from django_genericfilters.views import FilteredListView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status 
import json
from rest_framework.views import APIView
# Create your views here.

class CreateUser (generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    def post(self, request,format = None):
        
        user_data = UserSerializer(data = request.data)
        print(user_data)
        if user_data.is_valid():
            user_data.save()
            print(request.data['email'])
            user_object = user.objects.get(email=request.data['email'])
            user_object.set_password(request.data['password'])
            user_object.save()
            serializer=UserSerializer(user_object)
            return Response({"message":"user registered sccessfully",'userData':serializer.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":user_data.errors,"status ": status.HTTP_400_BAD_REQUEST})  
    
    def get(self, request,format = None): 
            try:
                user_data = user.objects.all()
                serializer=UserSerializer(user_data,many=True)
                return Response({"data":serializer.data,"status ": status.HTTP_201_CREATED})
            except user.DoesNotExist:
                return Response({"data":"table not exists","status ": status.HTTP_401_UNAUTHORIZED})
                 
           
  
class UpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
        queryset = user.objects.all()
        serializer_class = UserSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['=email']

        def patch(self, request, *args, **kwargs):
            user_data= user.objects.get(email=kwargs["pk"])
            user_data.set_password(request.data['password'])
            user_data.save()
            serializer=UserSerializer(user_data)
            return Response({"message":"Password has been changed","data":serializer.data,"status ": status.HTTP_201_CREATED})
        
class seachThroughRole(generics.ListAPIView):
        queryset = user.objects.all()
        serializer_class = UserSerializer
        def get(self, request, *args, **kwargs):
            if str(kwargs['role']).capitalize() == "Teacher":
                queryset = user.objects.filter(is_teacher=True,is_guid=False,is_AICTEmember=False,is_dean=False,is_hod=False,is_student=False)
            elif str(kwargs['role']).capitalize()== "Guid":
                queryset = user.objects.filter(is_guid=True,is_teacher=False,is_AICTEmember=False,is_dean=False,is_hod=False,is_student=False)
            elif str(kwargs['role']).capitalize() == "Hod":
                queryset = user.objects.filter(is_AICTEmember=False,is_teacher=False,is_guid=False,is_dean=False,is_hod=True,is_student=False)
            elif str(kwargs['role']).capitalize() == "Dean":
                queryset = user.objects.filter(is_dean=True,is_teacher=False,is_guid=False,is_AICTEmember=False,is_hod=False,is_student=False)
            elif str(kwargs['role']).capitalize() == "Aictemember":
                queryset = user.objects.filter(is_hod=False,is_teacher=False,is_guid=False,is_AICTEmember=True,is_dean=False,is_student=False)
            elif str(kwargs['role']).capitalize() == "Student":
                queryset = user.objects.filter(is_student=True,is_teacher=False,is_guid=False,is_AICTEmember=False,is_dean=False,is_hod=False)
            serializer=UserSerializer(queryset,many=True)
            return Response({'data':serializer.data,'status':status.HTTP_200_OK}) 
            
class deleteAll(generics.DestroyAPIView):
     queryset=user.objects.all()
     serializer_class=UserSerializer
     def post(self, request, *args, **kwargs):
           data = user.objects.all()
           data.delete()
           return Response({'status':status.HTTP_200_OK})
class RoleInfo(generics.ListCreateAPIView):
     queryset=role.objects.all()
     serializer_class=UserSerializer

class RoleDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset=role.objects.all()
        serializer_class=UserSerializer
        serializer_class = UserSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['=id']