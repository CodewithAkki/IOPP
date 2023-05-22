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



class role(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)

class University(models.Model):
    id=models.AutoField(primary_key=True)
    UniversityName=models.CharField(max_length=200,null=True,default=" ")

class college(models.Model):
    code = models.AutoField(primary_key=True)
    collegeName=models.CharField(max_length=200,null=True,default=" ")
    Type=models.CharField(max_length=200,null=True,default=" ")
    University=models.ForeignKey(University,on_delete=CASCADE)


class user (AbstractUser):
    #username = models.CharField(max_length=200,unique=True)
    username = None
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200,null=True,default=" ")
    last_name = models.CharField(max_length=200,null=True,default=" ")
    college =models.ForeignKey(college,on_delete=CASCADE)
    department=models.CharField(max_length=200,null=True,default=" ",blank=True)
    university= models.ForeignKey(University,on_delete=CASCADE)
    phone_no = models.CharField(max_length=15,null=True,default=None)
    address=models.CharField(max_length=200,null=True,default=" ")
    birthdate=models.DateField(null=True,default=None)
    email =models.EmailField(_('email address'),unique=True)
    role=models.ForeignKey(role,on_delete=CASCADE)
    profilePic = models.URLField(max_length=200,default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    registerDate = models.DateField(auto_now=True)
    githublink=models.CharField(max_length=200,default="github",blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=CustomUserManager()


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created=False,**kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print('Token:- ', token.key)



    