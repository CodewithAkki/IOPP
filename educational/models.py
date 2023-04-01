from django.db import models
from django.db.models.deletion import CASCADE
import uuid
# Create your models here.
class University (models.Model):
    registration_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=15,null=True,blank=True)
    state = models.CharField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=500,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name

class college (models.Model):
    registation_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    accrediation = models.CharField(max_length=500)
    approvals = models.CharField(max_length=500)
    grads = models.CharField(max_length=7)
    contact_no = models.CharField(max_length=15,null=True,blank=True)
    state = models.CharField(max_length=500,null=True,blank=True)
    city = models.CharField(max_length=500,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    university = models.ForeignKey(University,on_delete=CASCADE)
    def __str__(self):
        return self.name
