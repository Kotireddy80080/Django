from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)