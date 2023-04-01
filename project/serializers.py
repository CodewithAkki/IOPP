from rest_framework import serializers
from .models import Goal,Milestone,Domain,Project,Repository,Group,Approval

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
        model=Approval
        fields = '__all__'

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Repository
        fields = '__all__'

class GroupSerializer (serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = '__all__'

