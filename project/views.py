from django.shortcuts import render
from .models import Goal,Milestone,Domain,Project,Group,Approve,Assignment
from .serializers import AssignmentSerializer,GoalSerializer,DomainstoneSerializer,ProjectSerializer,ApprovalSerializer,MailestoneSerializer,GroupSerializer,DomainstoneSerializer 
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.models import role
from users.models import user


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

class UpdateDeleteRetriveProject(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']

    def get(self, request, *args, **kwargs):
        project=Project.objects.get(id=kwargs["id"])
        group=Group.objects.get(id=kwargs["id"])
        serializer=ProjectSerializer(project)
        print(serializer.data)
        serializer.data
        serializer.data["Group"]
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