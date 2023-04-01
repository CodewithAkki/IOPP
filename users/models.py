from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.conf import settings
from django.db.models.signals import  post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager

from django.db.models.deletion import CASCADE
class user (AbstractUser):
    #username = models.CharField(max_length=200,unique=True)
    username = None
    first_name = models.CharField(max_length=200,null=True,default=" ")
    last_name = models.CharField(max_length=200,null=True,default=" ")
    college =models.CharField(max_length=200,null=True,default=" ")
    department=models.CharField(max_length=200,null=True,default=" ",blank=True)
    designation= models.CharField(max_length=200,default=" ",null=True,blank=True)
    phone_no = models.CharField(max_length=15,null=True,default=None)
    address=models.CharField(max_length=200,null=True,default=" ")
    birthdate=models.DateField(null=True,default=None)
    email =models.EmailField(_('email address'),unique=True)
    is_teacher=models.BooleanField(default=False)
    is_guid=models.BooleanField(default=False)
    is_AICTEmember=models.BooleanField(default=False)
    is_dean=models.BooleanField(default=False)
    is_hod=models.BooleanField(default=False)
    profilePic = models.URLField(max_length=200,default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    registerDate = models.DateField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=CustomUserManager()


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created=False,**kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print('Token:- ', token.key)

