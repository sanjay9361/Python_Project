from django.db import models

# Create your models here.
class Products(models.Model):
    Name=models.CharField(max_length=50)
    price=models.IntegerField()