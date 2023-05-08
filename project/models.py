from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from users.models import user 
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


class GroupName(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,blank=False,null=True,unique=True)

class Project (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name=models.CharField(max_length=200) 
    is_patent=models.BooleanField(default=False)
    patent_info=models.CharField(max_length=500,default=" ",null=True,blank=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateField()
    Storage_link = models.URLField(null=True,blank=True)
    type=models.CharField(max_length=10 , default='public')
    domain = models.ForeignKey(Domain,null=True,blank=False,on_delete=CASCADE)
    description = models.TextField()
    #leader = models.ForeignKey(user,on_delete=CASCADE,related_name="group_leader")
    #user1 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user1")
    #user2 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user2")
    #user3 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user3")
    #user4 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user4")
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','user'], name='Unique_entries_project')
        ]

class Group (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    #user1 = models.ForeignKey(user,on_delete=CASCADE,related_name="group_user1",null=True,blank=True)
    #user2 = models.ForeignKey(user,on_delete=CASCADE,related_name="group_user2",null=True,blank=True)
    #user3 = models.ForeignKey(user,on_delete=CASCADE,related_name="group_user3",null=True,blank=True)
    #user4 = models.ForeignKey(user,on_delete=CASCADE,related_name="group_user4",null=True,blank=True)
    #user5 = models.ForeignKey(user,on_delete=CASCADE,related_name="group_user5",null=True,blank=True)
    #user_project=models.ForeignKey(Project,on_delete=CASCADE , related_name="participent_project")
    



   


class Assignment(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    guid=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='guid')
    teacher=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='teacher')
    hod=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='hod')
    dean=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='dean')
    AicteMember=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='AicteMember')
    project = models.ForeignKey(Project,null=True,blank=False,on_delete=CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['guid','teacher','hod','dean','AicteMember','project'], name='Unique_entries_assigned')
        ]

class Approve(models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    is_approved_guid = models.BooleanField(default=False)
    is_aicte_approved= models.BooleanField(default=False)
    is_hod_approved= models.BooleanField(default=False)
    is_dean_approved= models.BooleanField(default=False)
    is_teacher_approved=models.BooleanField(default=False)
    project=models.ForeignKey(Project,on_delete=CASCADE)
    description_guid=models.CharField(max_length=1000,null=True,blank=False)
    description_hod=models.CharField(max_length=1000,null=True,blank=False)
    description_dean=models.CharField(max_length=1000,null=True,blank=False)
    description_aicte=models.CharField(max_length=1000,null=True,blank=False)
    description_teacher=models.CharField(max_length=1000,null=True,blank=False)

    def __str__(self):
        return self.project