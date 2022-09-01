from django.db import models
from userapi.models import User
# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    creator= models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    #issue=models.ForeignKey(Issue,blank=True,null=True,on_delete=models.CASCADE)
    #creator = models.CharField(max_length=100)
    #class Meta:
        #managed = True
        #db_table = 'db_user'

    #def __str__(self):
     #   return str(self.creator)
# Create your models here.