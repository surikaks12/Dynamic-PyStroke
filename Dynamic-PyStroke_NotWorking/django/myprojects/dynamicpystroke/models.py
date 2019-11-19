from django.db import models

# Create your models here.
class UserData(models.Model):
    username= models.CharField(max_length=100)
    userkey= models.CharField(max_length=6, primary_key=True)
    password= models.CharField(max_length=10000)
