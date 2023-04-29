from .models import user
from rest_framework import serializers

class UserSerializer (serializers.ModelSerializer):
     class Meta:
        model = user
        fields = [
            
            'first_name',
            'last_name',
            'college',
            'department',
            'designation',
            'phone_no',
            'address',
            'birthdate',
            'email',
            'password',
            'is_teacher',
            'is_guid',
            'is_AICTEmember',
            'is_dean',
            'is_hod',
            'profilePic',
            
            ]
