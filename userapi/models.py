from django.db import models
class User(models.Model):
    userName = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.email)
# Create your models here.
