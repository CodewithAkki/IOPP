from django.shortcuts import render
from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer
# Create your views here.
class Event_info(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class Event_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
