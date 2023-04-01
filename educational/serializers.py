from .models import college , University
from rest_framework import serializers

class collegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = college
        fields = '__all__'


class universitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
