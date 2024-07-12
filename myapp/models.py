from django.db import models

# Create your models here.
class custumers(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    age=models.IntegerField()