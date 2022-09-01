from rest_framework import viewsets

from . import models

from . import serializers

class TypeViewset(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
    
'''    def get_queryset(self):
            req = self.request
            print(req)
            title = req.query_params.get('title')
            if title:
                self.queryset = models.Project.objects.filter(title=title)
                return self.queryset
            else:
                return self.queryset

'''
