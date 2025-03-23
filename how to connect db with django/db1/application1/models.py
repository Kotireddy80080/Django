from django.db import models
class students(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=21)
    subject=models.CharField(max_length=21)
    marks=models.FloatField()
    email=models.EmailField()
