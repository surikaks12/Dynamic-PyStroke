from django.db import models

# Create your models here.
class UserData(model.Model):
    username= models.CharField(max_length=100)
    userkey= models.CharField(max_length=6, primary_key=True, default=pkgen)
    password= models.CharField(max_length=10000)
