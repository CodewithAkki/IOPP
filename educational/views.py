from django.shortcuts import render
from .serializers import collegeSerializer,universitySerializer
from .models import college , University
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
# Create your views here.

class CreatecCollege(generics.ListCreateAPIView):
    
    queryset = college.objects.all()
    serializer_class = collegeSerializer

class UpdateDeleteRetriveCollege(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = college.objects.all()
    serializer_class = collegeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class CreatecUniversity(generics.ListCreateAPIView):
  
    queryset = University.objects.all()
    serializer_class = universitySerializer

class UpdateDeleteRetriveUniversity(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = University.objects.all()
    serializer_class = universitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']
