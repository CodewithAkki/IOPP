from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from users.models import user
from django.dispatch import receiver 
from django.db.models.signals import  post_save

# Create your models here.
class Goal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid4)
    name = models.CharField(max_length=200,null=True,blank=False)
    description = models.TextField()
    startDate = models.DateTimeField(auto_now=True)
    EndDate = models.DateField()
    status = models.CharField(max_length=7)
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
    patentNo=models.IntegerField(null=True,blank=True)
    AcademicYear=models.CharField(max_length=4) 
    semester=models.CharField(max_length=20)
    patent_info=models.TextField(default=" ",null=True,blank=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateField()
    Storage_link = models.URLField(null=True,blank=True)
    type=models.CharField(max_length=10 , default='public')
    domain = models.ForeignKey(Domain,null=True,blank=False,on_delete=CASCADE)
    description = models.TextField()
    message = models.TextField(default="",blank=False)
    isapproval=models.CharField(max_length=100 , default='Not Approved')
    leader=models.ForeignKey(user,on_delete=CASCADE,related_name="leader_project",blank=True)
    guid=models.ForeignKey(user,on_delete=CASCADE,related_name="guid_project",blank=True,null=True)
    hod=models.ForeignKey(user,on_delete=CASCADE,related_name="hod_project",blank=True,null=True)
    dean=models.ForeignKey(user,on_delete=CASCADE,related_name="dean_project",blank=True,null=True)
    aicte=models.ForeignKey(user,on_delete=CASCADE,related_name="aicte_project",blank=True,null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='Unique_entries_project')
        ]
@receiver(post_save,sender=Project)
def create_auth_token(sender,instance = None,created=False,**kwargs):
    if created:
        try:
            project = Project.objects.get(user=instance.id)
            hod=user.objects.get(role=3,college=project.leader.college.code)
            dean=user.objects.get(role=4,college=project.leader.college.code)
            project.hod=hod
            project.dean=dean
            project.save()
            
        except:
                pass

class Assignment(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    guid=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='guid')
    hod=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='hod')
    dean=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='dean')
    AicteMember=models.ForeignKey(user,null=True,blank=False,on_delete=CASCADE,related_name='AicteMember')
    project = models.ForeignKey(Project,null=True,blank=False,on_delete=CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['guid','hod','dean','AicteMember','project'], name='Unique_entries_assigned')
        ]

class HodApproval(models.Model):
    id=models.AutoField(primary_key=True)
    hod=models.ForeignKey(user,on_delete=CASCADE,blank=True,null=True)
    project=models.ForeignKey(Project,on_delete=CASCADE,blank=True,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['hod','project'],name="uniqueHodApproval")
        ] 
class DeanApproval(models.Model):
    id=models.AutoField(primary_key=True)
    Dean=models.ForeignKey(user,on_delete=CASCADE,blank=True,null=True)
    project=models.ForeignKey(Project,on_delete=CASCADE,blank=True,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['Dean','project'],name="uniqueDeanApproval")
        ]  
class AicteApproval(models.Model):
    id=models.AutoField(primary_key=True)
    Aicte=models.ForeignKey(user,on_delete=CASCADE,blank=True,null=True)
    project=models.ForeignKey(Project,on_delete=CASCADE,blank=True,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['Aicte','project'],name="uniqueAicteApproval")
        ] 

'''
  {
    "id": 1,
    "name": "Student"
  },
  {
    "id": 2,
    "name": "Guid"
  },
  {
    "id": 3,
    "name": "Hod"
  },
  {
    "id": 4,
    "name": "Aicte member"
  },
  {
    "id": 5,
    "name": "Dean"
  }
'''

class Group (models.Model):
    id= models.UUIDField(primary_key=True,editable=False,default=uuid4)
    leader = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_leader")
    user1 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user1")
    user2 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user2")
    user3 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user3")
    user4 = models.ForeignKey(user,on_delete=CASCADE,null=True,blank=True,related_name="group_user4")
    project=models.ForeignKey(Project,on_delete=CASCADE,null=True,blank=True,related_name="Group_project")
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project'], name='group_project')
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
    

class guidrecord(models.Model):
    id=models.AutoField(primary_key=True)
    guid=models.ForeignKey(user,on_delete=CASCADE,related_name="guidrecord")
    project=models.ForeignKey(Project,on_delete=CASCADE,related_name="guidprojectrecord")
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['guid','project'],name="guidrecordunique")
        ]
class hodrecord(models.Model):
    id=models.AutoField(primary_key=True)
    hod=models.ForeignKey(user,on_delete=CASCADE,related_name="hodrecord")
    project=models.ForeignKey(Project,on_delete=CASCADE,related_name="hodprojectrecord")
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['hod','project'],name="hodrecordunique")
        ]
class deanrecord(models.Model):
    id=models.AutoField(primary_key=True)
    dean=models.ForeignKey(user,on_delete=CASCADE,related_name="deanrecord")
    project=models.ForeignKey(Project,on_delete=CASCADE,related_name="deanprojectrecord")
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['dean','project'],name="deanrecordunique")
        ]
class aicterecord(models.Model):
    id=models.AutoField(primary_key=True)
    aicte=models.ForeignKey(user,on_delete=CASCADE,related_name="aicterecord")
    project=models.ForeignKey(Project,on_delete=CASCADE,related_name="aicteprojectrecord")
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['aicte','project'],name="aicterecordunique")
        ]