from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from users.models import user as user
# Create your models here.
class Goal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid4)
    name = models.CharField(max_length=200,null=True,blank=False)
    description = models.TextField()
    startDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateField()
    status = models.CharField(max_length=7,)
    def __str__(self):
        return self.name

class Milestone (models.Model):
    id = models.UUIDField(primary_key=True,editable=True,default=uuid4)
    name = models.CharField(max_length=200,null=True,blank=False)
    description = models.TextField()
    goal = models.ForeignKey(Goal,on_delete=CASCADE,null=True,blank=False)
    startDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateField()
    status = models.CharField(max_length=7)
    def __str__(self):
        return self.name



class Domain (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name = models.CharField(max_length=200)
    description=models.TextField()



class Project (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name=models.CharField(max_length=200) 
    is_patent=models.BooleanField(default=False)
    patent_info=models.CharField(max_length=500,default=" ",null=True,blank=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateField()
    goal =models.ForeignKey(Goal,on_delete=CASCADE)
    domain = models.ForeignKey(Domain,null=True,blank=False,on_delete=CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Approve(models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    is_approved_guid = models.BooleanField(default=False)
    is_aicte_approved= models.BooleanField(default=False)
    is_hod_approved= models.BooleanField(default=False)
    is_dean_approved= models.BooleanField(default=False)
    project=models.ForeignKey(Project,on_delete=CASCADE)
    description_guid=models.CharField(max_length=1000,null=True,blank=False)
    description_hod=models.CharField(max_length=1000,null=True,blank=False)
    description_dean=models.CharField(max_length=1000,null=True,blank=False)
    description_aicte=models.CharField(max_length=1000,null=True,blank=False)

    def __str__(self):
        return self.project
    
class Repository(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name=models.CharField(max_length=200,null=True,blank=False)
    project=models.OneToOneField(Project,on_delete=CASCADE)
    Storage_link = models.URLField(null=True,blank=True)
    type=models.CharField(max_length=10 , default='public')

    def __str__(self):
        return self.name

class Group (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name = models.CharField(max_length=200,blank=False,null=True)
    role = models.CharField(max_length=200,blank=False,null=True)
    student = models.ForeignKey(user,on_delete=CASCADE)
    project = models.ForeignKey(Project,on_delete=CASCADE)
    guid = models.ForeignKey(user,on_delete=CASCADE)

    def __str__(self):
        return self.name

class Approval (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    guid = models.ForeignKey(user,on_delete=CASCADE)
    group =models.ForeignKey(Group,on_delete=CASCADE) 
    project = models.ForeignKey(Project,on_delete=CASCADE)
    feedback = models.TextField()
    status = models.CharField(max_length=7) 
    def __str__(self):
        return self.project

