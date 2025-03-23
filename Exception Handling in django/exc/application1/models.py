from django.db import models
class product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=21)
    price=models.FloatField()
    company=models.CharField(max_length=21)
    m_date=models.DateField()
    e_date=models.DateField()
