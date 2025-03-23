from django.db import models
class products(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=21)
    price=models.FloatField()
    company=models.CharField(max_length=21)
    m_date=models.DateField()
    e_date=models.DateField()
class customers(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=21)
    address=models.CharField(max_length=21)
    mobile=models.CharField(max_length=15)
    email=models.EmailField()
    product=models.ManyToManyField(products)
