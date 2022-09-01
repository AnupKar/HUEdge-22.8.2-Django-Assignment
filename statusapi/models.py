from django.db import models
class Status(models.Model):
    status = models.CharField(max_length=100)
    
    #def __str__(self):
      #return str(self.id)
# Create your models here.
