from .models import user,role,college,University
from rest_framework import serializers

class UserSerializer (serializers.ModelSerializer):
     class Meta:
        model = user
        fields = [
            'id',
            'first_name',
            'last_name',
            'college',
            'department',
            'university',
            'phone_no',
            'address',
            'birthdate',
            'email',
            'password',
            'role',
            'profilePic',
           
            ]
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = college
        fields='__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields='__all__'

