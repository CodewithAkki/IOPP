from rest_framework import serializers
from .models import hodrecord,deanrecord, aicterecord ,guidrecord, Goal,Milestone,Assignment,Domain,Project,Group,Approve

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

class guidrecordSerilizer(serializers.ModelSerializer):
    class Meta:
        model=guidrecord
        field='__all__'
class hodrecordSerilizer(serializers.ModelSerializer):
    class Meta:
        model=hodrecord
        field='__all__'
class deanrecordSerilizer(serializers.ModelSerializer):
    class Meta:
        model=deanrecord
        field='__all__'
class aicterecordSerilizer(serializers.ModelSerializer):
    class Meta:
        model=aicterecord
        field='__all__'
class GroupSerializer (serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = '__all__'

class AssignmentSerializer (serializers.ModelSerializer):
    class Meta:
        model=Assignment
        fields = '__all__'
