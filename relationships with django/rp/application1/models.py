from django.db import models
class place(models.Model):
    name=models.CharField(max_length=21)
    address=models.CharField(max_length=21)
class hotel(models.Model):
    place=models.OneToOneField(place,on_delete=models.CASCADE,primary_key=True)
class waiters(models.Model):
    first_name=models.CharField(max_length=21)
    last_name=models.CharField(max_length=21)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    
