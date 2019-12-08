from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDatas(models.Model):
    Email1= models.CharField(max_length=100)
    Password1= models.CharField(max_length=10000)
