from django.db import models
class employees(models.Model):
    first_name=models.CharField(max_length=21)
    last_name=models.CharField(max_length=21)
    username=models.CharField(max_length=21)
    p1=models.CharField(max_length=21)
    p2=models.CharField(max_length=21)
    email=models.EmailField()
