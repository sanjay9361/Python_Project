from django.db import models

# Create your models here.

class Sports(models.Model):
    Name=models.CharField(max_length=50)
    Time=models.IntegerField(null=True)
    Image=models.ImageField(null=True)