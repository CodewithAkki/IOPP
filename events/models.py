from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Event (models.Model):
    name = models.CharField(max_length=200 , null= True , blank=True)
    startDate= models.DateTimeField(_("Date"), auto_now_add=True,null= True , blank=True)
    EndDate = models.DateTimeField(null= True , blank=True)
    description= models.TextField(null= True , blank=True)
    link= models.URLField(null= True , blank=True)
    event_picture=models.UUIDField(null= True , blank=True)

    def __str__(self):
        return self.name
        