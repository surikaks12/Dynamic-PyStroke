from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDatas(models.Model):
    Email= models.CharField(max_length=100)
    Password= models.CharField(max_length=10000)
