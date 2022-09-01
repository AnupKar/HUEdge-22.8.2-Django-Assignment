from rest_framework import viewsets

from . import models

from . import serializers

class IssueViewset(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    def get_queryset(self):
            req = self.request
            print(req)
            title = req.query_params.get('title')
            if title:
                self.queryset = models.Issue.objects.filter(title=title)
                return self.queryset
            else:
                return self.queryset
