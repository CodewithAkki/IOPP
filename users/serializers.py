from .models import user,role
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
            'is_student'
            ]
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields='__all__'
