from rest_framework import serializers
from .models import Goal,Milestone,Assignment,Domain,Project,Repository,Group,Approve

class GoalSerializer (serializers.ModelSerializer):
    class Meta:
        model=Goal
        fields = '__all__'

class MailestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Milestone
        fields = '__all__'

class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = '__all__'

class DomainstoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Domain
        fields = '__all__'
class ApprovalSerializer (serializers.ModelSerializer):
    class Meta:
        model=Approve
        fields = '__all__'

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Repository
        fields = '__all__'

class GroupSerializer (serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = '__all__'

class AssignmentSerializer (serializers.ModelSerializer):
    class Meta:
        model=Assignment
        fields = '__all__'
