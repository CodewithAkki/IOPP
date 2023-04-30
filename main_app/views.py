from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from users.models import user
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import role
class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            user_data=user.objects.get(email=request.data['username'])
            if user_data:
                if user_data.check_password(request.data['password']) :
                    token,t=Token.objects.get_or_create(user=user_data)
                    print(t,token)
                    print(user_data.role.id)
                    print(user_data.profilePic)
                    userRole=role.objects.get(id=user_data.role.id)

                    return Response({
                    "message":'login successfully',
                    'token': token.key,
                    'userId': user_data.pk,
                    'email': user_data.email,
                    'role':userRole.name,
                    'first_name':user_data.first_name,
                    'last_name':user_data.last_name,
                    'college':user_data.college,
                    'picture':user_data.profilePic
                    })
                else:
                     return Response({
                "message":'password doesnot match',
                }) 
            else:
                return Response({
                "message":'fail to login',
                })
        except user.DoesNotExist:
             return Response({
                "message":'fail to login',
                })
        