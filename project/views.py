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
    filter_backends=[filters.SearchFilter]
    search_fields=['=id']
class SearchDeleteGroup(generics.ListAPIView , generics.DestroyAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    def get(self, request, *args, **kwargs):
        group=Group.objects.filter(name=kwargs['name'])
        print(group)
        serializer=GroupSerializer(group,many=True)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})
    
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
            assignment=Assignment.objects.get(guid=kwargs['id_role'])
        elif str(name).capitalize() == "Teacher":
            assignment=Assignment.objects.get(teacher=kwargs['id_role'])
        elif str(name).capitalize() == "Hod":
            assignment=Assignment.objects.get(hod=kwargs['id_role'])
        elif str(name).capitalize() == "Dean":
            assignment=Assignment.objects.get(dean=kwargs['id_role'])
        elif str(name).capitalize() == "Aicte member":
            assignment=Assignment.objects.get(AicteMember=kwargs['id_role'])
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