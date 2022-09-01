from dataclasses import field
from rest_framework import serializers

from .models import Issue

from projectapi.serializers import ProjectSerializer
from userapi.serializers import UserSerializer
class IssueSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer()
    class Meta:
        model = Issue
        fields = '__all__'
        
class IssueWithProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    reporter = UserSerializer()
    class Meta:
        model = Issue
        fields = '__all__'
'''class IssueWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Issue
        fields = '__all__'
'''
