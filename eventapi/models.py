from django.db import models
from issueapi.models import Issue
from userapi.models import User
# Create your models here.
class Event(models.Model):
    logged_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    updated_field = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_value = models.CharField(max_length=400,null=True)
    new_value = models.CharField(max_length=400)
    
