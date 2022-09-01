from dataclasses import field
from rest_framework import serializers
#from userapi.serializers import UserSerializer
from .models import Type

class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type
        fields = '__all__'

'''class ProjectWithUserSerializer(serializers.ModelSerializer):
    creator=UserSerializer()
    class Meta:
        model = Project
        fields = '__all__'   '''
    #def __str__(self):
    #  return str(self.id) 