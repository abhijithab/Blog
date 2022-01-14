from django.db import models

# Create your models here.
class blog(models.Model):
    date=models.DateTimeField()
    blog=models.CharField(max_length=1000)

class post(models.Model):
    date = models.DateTimeField(null=True,blank=True)
    blog = models.CharField(max_length=1000 ,null=True,blank=True)
