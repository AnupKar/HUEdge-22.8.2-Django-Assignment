from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from .models import Issue
from .serializers import IssueWithProjectSerializer,IssueSerializer
from eventapi.serializers import EventSerializer
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
from rest_framework import status,filters
from django_filters.rest_framework import DjangoFilterBackend


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
        
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = IssueSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueData(APIView):
    #queryset = Project.objects.all()
    #serializer_class = ProjectWithUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        issue = Issue.objects.all()
        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueDetailById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Issue.objects.get(id=id)
        except Issue.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = IssueSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        new_data=json.loads(request.body)
        serializer = IssueSerializer(snippet, data=new_data)
        if serializer.is_valid():
            
            old_data=Issue.objects.filter(id=id)
            s_data=IssueSerializer(old_data[0])
            updated_arr=[]
            for key in s_data.data:
                if s_data.data.get(key) != new_data.get(key):
                    updated_arr.append(key)
            for each in updated_arr:
                event_log_json  = {}
                event_log_json["issue"] = s_data.data.get("id")
                event_log_json["updated_field"] = each
                event_log_json["previous_value"] = s_data.data.get(each)
                event_log_json["new_value"] = new_data[each]
                event_log_json["logged_by"] = request.user.id
                serializer_new = EventSerializer(data=event_log_json)
                serializer_new.is_valid(raise_exception=True)
                serializer_new.save()
            #print("----:",request.user.id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IssueList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['id','description','title']
    search_fields=['id','description','title']
'''
@api_view(['GET'])
def getData(request):
    issues = Issue.objects.all()
    serializer = IssueWithProjectSerializer(issues, many=True)
    #print(json.dumps(serializer.data))
    return Response(serializer.data)
'''

# Create your views here.
