from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Issue
from .serializers import IssueWithProjectSerializer
import json
@api_view(['GET'])
def getData(request):
    issues = Issue.objects.all()
    serializer = IssueWithProjectSerializer(issues, many=True)
    #print(json.dumps(serializer.data))
    return Response(serializer.data)

# Create your views here.
