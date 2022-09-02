from operator import imod
from django.shortcuts import render
import json
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from .models import Project
from userapi.models import User
from .serializers import ProjectSerializer, ProjectWithUserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
'''
@api_view(['GET'])
def getData(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    return Response(serializer.data)
'''
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def getByTitle(request):
    title_req = request.GET.get('title')
    #print(title_req)
    items = Project.objects.filter(title__icontains=title_req)
    serializer = ProjectSerializer(items, many=True)
    return Response(serializer.data)

'''
@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getProjetcDetail(request):    
    projects = Project.objects.all()
    serializer = ProjectWithUserSerializer(projects, many=True)
    return Response(serializer.data)
'''
class ProjectDetails(APIView):
    #queryset = Project.objects.all()
    #serializer_class = ProjectWithUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectWithUserSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectWithUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProjectSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
@api_view(['GET'])
def getProjetcById(request,id):
    projects = Project.objects.get(id=id)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
'''
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
'''

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