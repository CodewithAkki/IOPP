from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from users.models import user
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user_data=user.objects.get(email=request.data['email'])
        if user_data.check_password(request.data['password']) :
            token,t=Token.objects.get_or_create(user=user_data)
            print(t,token)
            return Response({
            "message":'login successfully',
            'token': token.key,
            'userId': user_data.pk,
            'email': user_data.email
            })
        else:
            return Response({
            "message":'fail to login',
            })
        return Response({"status":status.HTTP_202_ACCEPTED})