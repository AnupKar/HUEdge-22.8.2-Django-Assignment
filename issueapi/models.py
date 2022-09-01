from django.db import models

from projectapi.models import Project
from userapi.models import User
# Create your models here.
# class Status(models.Model):
#     status = models.CharField(max_length=50)
#     id = models.IntegerField(primary_key=True)

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    Types = ('Bug',('Bug')),('Story',('Story')),('Task',('Task')),('Epic',('Epic'))
    Status = ('Open',('Open')),('InProgress',('In Progress')),('InReiew',('In Review')),('CodeComplete',('Code Complete')),('Done',('Done'))
    type = models.CharField(max_length=100,choices=Types,default='available')
    status = models.CharField(max_length=100,choices=Status,default='available')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.CharField(max_length=100)
    #assignee = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    reporter = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    #def __str__(self):
      #return str(self.id)

