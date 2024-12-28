from django.db import models

# Create your models here.

class Create(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.IntegerField(null=True)
    Imaage=models.ImageField(null=True)


class Types(models.Model):
    P_serial=models.ForeignKey(Create,null=True,on_delete=models.SET_NULL)
    Name=models.CharField(max_length=50)
    Price=models.IntegerField(null=True)
  