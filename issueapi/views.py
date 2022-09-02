from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from .models import Issue
from .serializers import IssueWithProjectSerializer
from operator import imod
import json
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from .models import Project
from userapi.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status



class IssueDetails(APIView):
    #queryset = Project.objects.all()
    #serializer_class = ProjectWithUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        issue = Issue.objects.all()
        serializer = IssueWithProjectSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IssueWithProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET'])
def getData(request):
    issues = Issue.objects.all()
    serializer = IssueWithProjectSerializer(issues, many=True)
    #print(json.dumps(serializer.data))
    return Response(serializer.data)
'''

# Create your views here.
