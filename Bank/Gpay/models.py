from django.db import models

# Create your models here.

class Foods(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.IntegerField(null=True)
    Image=models.ImageField(null=True)

class Bill_Items(models.Model):
    Bill_no=models.IntegerField()
    Product_name=models.CharField(max_length=40)
    total=models.IntegerField()