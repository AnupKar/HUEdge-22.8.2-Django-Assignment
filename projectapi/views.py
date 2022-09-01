from django.shortcuts import render
import json
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Project
from userapi.models import User
from .serializers import ProjectSerializer, ProjectWithUserSerializer

@api_view(['GET'])
def getData(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getByTitle(request):
    title_req = request.GET.get('title')
    #print(title_req)
    items = Project.objects.filter(title__icontains=title_req)
    serializer = ProjectSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProjetcDetail(request):
    projects = Project.objects.all()
    serializer = ProjectWithUserSerializer(projects, many=True)
    return Response(serializer.data)
'''
@api_view(['GET'])
def getProjetcById(request,id):
    projects = Project.objects.get(id=id)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
'''

@api_view(['DELETE'])
def deleteProject(request,id):
    project = Project.objects.get(id=id)
    project.delete()
    projects=Project.objects.all()
    serializer = ProjectWithUserSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateProjetcDetail(request,id):
    project = Project.objects.get(id=id)
    project.title=request.data.get("title")
    project.description=request.data.get("description")
    project.save()
    projects = Project.objects.all()
    serializer = ProjectWithUserSerializer(projects, many=True)
    return Response(serializer.data)


'''@api_view(['POST'])
def createProject(request):
    
    data=json.loads(request.body)
    project=ProjectWithUserSerializer(data=data)

    project.is_valid(raise_exception=True)
    project.save()
    projects = Project.objects.all()
    serializer = ProjectWithUserSerializer(projects, many=True)
    return Response(serializer.data) '''

class CreateProject(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id=request.data.get("creator")
        creator_obj=User.objects.get(id=id)
        serializer.save(creator=creator_obj)
        return Response(serializer.data)