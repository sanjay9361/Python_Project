from django.db import models

# Create your models here.


class Fund(models.Model):
    Name=models.CharField(max_length=45)
    Age=models.IntegerField(null=True)
    Number=models.IntegerField(null=True)

   


class Coopen(models.Model):
       P_id=models.ForeignKey(Fund,null=True,on_delete=models.SET_NULL)
       Name=models.CharField(max_length=45)
       Age=models.IntegerField(null=True)
       Number=models.IntegerField(null=True)
       Image=models.ImageField(null=True)
       


