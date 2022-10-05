from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
 
class Keeper(models.Model):
    user_name=models.CharField(max_length=30,blank=True)
    password=models.CharField(max_length=30,blank=True)
    platform=models.CharField(max_length=30,blank=True)

    def __str__(self):
     return self.platform
