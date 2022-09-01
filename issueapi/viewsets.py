from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class IssueViewset(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
            req = self.request
            print(req)
            title = req.query_params.get('title')
            if title:
                self.queryset = models.Issue.objects.filter(title=title)
                return self.queryset
            else:
                return self.queryset
