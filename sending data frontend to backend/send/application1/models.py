from django.db import models
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=21)
    subjects=models.CharField(max_length=21)
    marks=models.IntegerField()
    total=models.IntegerField()
