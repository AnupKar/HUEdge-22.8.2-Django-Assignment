from rest_framework import viewsets
from rest_framework import permissions
from . import models
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers

class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
            req = self.request
            print(req)
            title = req.query_params.get('title')
            if title:
                self.queryset = models.Project.objects.filter(title=title)
                return self.queryset
            else:
                return self.queryset
