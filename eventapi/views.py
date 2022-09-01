from asyncio import events
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from issueapi.models import Issue
from .serializers import EventSerializer
from .models import Event
class EventClass(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id=request.data.get("issue")
        issue_obj=Issue.objects.get(id=id)
        print("issue_obj: ",issue_obj)
        serializer.save(issue=issue_obj) #previous_value=issue_obj['title']
        return Response(serializer.data)

    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
        
# Create your views here.
