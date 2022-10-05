from django.db import models

# Create your models here.
class Boss(models.Model):
    your_todo=models.CharField(max_length=60)

def __str__(self):
    return self.your_todo
