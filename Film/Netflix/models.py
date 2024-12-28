from django.db import models

# Create your models here.

class Production(models.Model):
    Name=models.CharField(max_length=30)
    Price=models.IntegerField()
    Image=models.ImageField(null=True)