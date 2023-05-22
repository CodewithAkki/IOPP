from django.shortcuts import render
from .models import guidrecord,Goal,Milestone,Domain,Project,Group,Approve,Assignment,hodrecord,aicterecord,deanrecord
from .serializers import deanrecordSerilizer,aicterecordSerilizer,guidrecordSerilizer,hodrecordSerilizer,AssignmentSerializer,GoalSerializer,DomainstoneSerializer,ProjectSerializer,ApprovalSerializer,MailestoneSerializer,GroupSerializer,DomainstoneSerializer 
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from users.models import role
from users.models import user
import json

# Create your views here.
class CreateListGoal(generics.ListCreateAPIView):
    queryset=Goal.objects.all()
    serializer_class=GoalSerializer

class CreateMailestone(generics.ListCreateAPIView):
    queryset=Milestone.objects.all()
    serializer_class=MailestoneSerializer

class CreateListGroup(generics.ListCreateAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    def post(self, request, *args, **kwargs):
        print(request.data)
        leader=user.objects.get(email=request.data['leader'])
        user1=user.objects.get(email=request.data['user1'])
        user2=user.objects.get(email=request.data['user2'])
        user3=user.objects.get(email=request.data['user3'])
        user4=user.objects.get(email=request.data['user4'])
        project=Project.objects.get(id=request.data['project'])
        Group.objects.create(leader=leader,user1=user1,user2=user2,user3=user3,user4=user4,project=project)
        if Group.objects.get(project=project):
            return Response({"message":"group created","status":status.HTTP_200_OK})
        else:
            return Response({"message":"fail to register","status":status.HTTP_200_OK})

class CreateProject(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
import json
class CreateProject1(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.all()
        obj=dict()
        objlist=list()
        for obj1 in project:
            obj['id']=str(obj1.id)
            obj['name']=obj1.name
            obj['patentNo']=obj1.patentNo
            obj['AcademicYear']=obj1.AcademicYear
            obj['semester']=obj1.semester
            obj['patent_info']=obj1.patent_info
            obj['isapproved']=obj1.isapproval
            obj['start_date']=str(obj1.start_date)
            obj['end_date']=str(obj1.end_date)
            obj['Storage_link']=obj1.Storage_link
            obj['type']=obj1.type
            obj['domain']=obj1.domain.name
            obj['semester']=obj1.semester
            obj['description']=obj1.description
            obj['college']=obj1.leader.college.collegeName
            obj['state']=obj1.leader.address
            obj['university']=obj1.leader.university.UniversityName
            obj['department']=obj1.leader.department
            obj['message']=obj1.message
            obj['leader']=obj1.leader.first_name+" "+obj1.leader.last_name
            obj['guid']=obj1.guid.first_name+" "+obj1.guid.last_name
            obj['hod']=obj1.hod if obj1.hod==None else obj1.hod.first_name+" "+obj1.hod.last_name,
            obj['dean']=obj1.dean if obj1.dean==None else obj1.dean.first_name+" "+obj1.dean.last_name,
            obj['aicte']=obj1.aicte if obj1.aicte==None else obj1.aicte.first_name+" "+obj1.aicte.last_name,
            
            objlist.append(obj.copy())
            obj.clear()
        return HttpResponse(json.dumps(objlist),status=status.HTTP_200_OK)

class updateProject(generics.RetrieveUpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=pk']
    def patch(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['pk'])
        project.message=request.data['message']
        project.save()
        serializer=ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        

class projectguid(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
       project= Project.objects.filter(guid=kwargs['guid'])
       guid=user.objects.get(id=kwargs['guid'])
       for i in project:
            Assignment.objects.get_or_create(project=i,guid=guid)
       serializer=ProjectSerializer(project,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)

class CreateListApprove(generics.ListCreateAPIView):
    queryset=Approve.objects.all()
    serializer_class=ApprovalSerializer

class CreateListDomain(generics.ListCreateAPIView):
    queryset=Domain.objects.all()
    serializer_class=DomainstoneSerializer



class UpdateDeleteRetriveGoal(generics.RetrieveUpdateDestroyAPIView):
    queryset=Goal.objects.all()
    serializer_class=GoalSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']

class UpdateDeleteRetriveMailestone(generics.RetrieveUpdateDestroyAPIView):
    queryset=Milestone.objects.all()
    serializer_class=MailestoneSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']

class UpdateDeleteRetriveGroup(generics.RetrieveUpdateDestroyAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    def get(self, request, *args, **kwargs):
        try:
            import json
            group=Group.objects.get(project=kwargs['project'])
            seriaizer=GroupSerializer(group)
            data=seriaizer.data
            collect=dict()
            collect['leader']=user.objects.get(id=data['leader']).email
            collect['user1']=user.objects.get(id=data['user1']).email
            collect['user2']=user.objects.get(id=data['user2']).email
            collect['user3']=user.objects.get(id=data['user3']).email
            collect['user4']=user.objects.get(id=data['user4']).email
            
            
            print(collect)
            seri=json.loads(json.dumps(collect,indent = 7))

            return Response(seri,status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, *args, **kwargs):
        try:
            group=Group.objects.get(kwargs['project'])
            seriaizer=GroupSerializer(group,data=request.data,partial=True)
            return Response(seriaizer.data,status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({"data": "does not exists","status":status.HTTP_400_BAD_REQUEST})

    
    def delete(self, request, *args, **kwargs):
        group=Group.objects.filter(name=kwargs['name'])
        group.delete()
        return Response({'data':'deleted','status':status.HTTP_200_OK})

class AssignmentGuidsDetail(generics.ListCreateAPIView):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer

class AssignmentGuidsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']

class UpdateDeleteRetriveDomain(generics.RetrieveUpdateDestroyAPIView):
    queryset=Domain.objects.all()
    serializer_class=DomainstoneSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']
class UpdateSINGLEProject(generics.RetrieveUpdateDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=pk']
    
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['pk'])
        
        return Response({
            "AcademicYear": project.AcademicYear,
"Storage_link": project.Storage_link,
"aicte": project.aicte,
"dean": project.dean,
"description": project.description,
"domain": project.domain.name,
"end_date": project.end_date,
"guid": project.guid.first_name+" "+project.guid.last_name,
"department":project.guid.department,
"hod": "" if project.hod==None else project.hod.first_name+" "+project.hod.last_name,
"id": project.id,
"leader": project.leader.first_name+" "+project.leader.last_name,
"name": project.name,
"patentNo": project.patentNo,
"patent_info": project.patent_info,
"semester": project.semester,
"start_date": project.start_date,
"type": project.type
},status=status.HTTP_200_OK)
    


class UpdateDeleteRetriveProject(generics.RetrieveUpdateDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']
    def patch(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs["id"])
        serializer=ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs["id"])
        group=Group.objects.get(id=kwargs["id"])
        serializer=ProjectSerializer(project)
        print(serializer.data)
        serializer.data
        serializer.data["Group"]
        return Response({"data":serializer.data,"status":status.HTTP_201_CREATED})
    def delete(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs["id"])
        serializer=ProjectSerializer(project)
        project.delete()
        return Response({"data":serializer.data,"status":status.HTTP_201_CREATED})
    


class UpdateDeleteRetriveApproval(generics.RetrieveUpdateDestroyAPIView):
   
    queryset=Approve.objects.all()
    serializer_class=ApprovalSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']

class AssignedProjects(generics.ListAPIView):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer

    def get(self, request, *args, **kwargs):
        name=kwargs['role']
        if str(name).capitalize() == "Guid":
            assignment=Assignment.objects.get(guid=kwargs['userid'])
        elif str(name).capitalize() == "Hod":
            assignment=Assignment.objects.get(hod=kwargs['userid'])
        elif str(name).capitalize() == "Dean":
            assignment=Assignment.objects.get(dean=kwargs['userid'])
        elif str(name).capitalize() == "Aicte member":
            assignment=Assignment.objects.get(AicteMember=kwargs['userid'])
        elif str(name).capitalize() == "Student":
            Project.object.filter()
        data=Project.objects.filter(id=assignment.project.id)
        serializer=ProjectSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class searchByproject(generics.ListAPIView):
    queryset=Approve.objects.all()
    serializer_class=ApprovalSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['project'])
        approve=Approve.objects.get(project=project)
        serializer=ApprovalSerializer(approve,data=request.data,partial=True)
        return Response(serializer.data)
class searchproject(generics.RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.filter(guid=kwargs['guid'])
        serializer=ProjectSerializer(project,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class guidtohod(generics.ListAPIView,generics.DestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        Hod=role.objects.get(name="Hod")
        userdata=user.objects.get(college=kwargs['college'],role=Hod)
        userguid=user.objects.get(id=2)
        guidrecord.objects.get_or_create(guid=userguid,project=project)
        project.guid=None
        project.hod=userdata
        project.save()
        
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        guids=guidrecord.objects.get(project=project)
        userdean=user.objects.get(id=guids.guid.id)
        project.guid=userdean
        project.hod=None
        project.save()
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class hodtodean(generics.ListAPIView, generics.DestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        Dean=role.objects.get(name="Dean")
        userdata=user.objects.get(college=kwargs['college'],role=Dean)
        userhod=user.objects.get(id=project.hod.id)
        hodrecord.objects.get_or_create(hod=userhod,project=project)
        project.hod=None
        project.dean=userdata
        project.save()
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        hods=hodrecord.objects.get(project=project)
        userdean=user.objects.get(id=hods.hod.id)
        project.hod=userdean
        project.dean=None
        project.save()
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)

class deantoAicte(generics.ListAPIView,generics.DestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        Aicte=role.objects.get(name="Aicte member")
        userdata=user.objects.get(college=kwargs['college'],role=Aicte)
        userdean=user.objects.get(id=project.dean.id)
        deanrecord.objects.get_or_create(dean=userdean,project=project)
        project.dean=None
        project.aicte=userdata
        project.save()
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)  
    def delete(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['id'])
        deans=deanrecord.objects.get(project=project)
        print(deans.dean.id)
        userdean=user.objects.get(id=deans.dean.id)
        project.dean=userdean
        project.aicte=None
        project.save()
        serializer=ProjectSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
  
class updateprojectdata(generics.UpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=pk']
    def patch(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs['pk'])
        serializer=ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)