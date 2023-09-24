from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser,PermissionsMixin):
    reg_no = models.CharField(max_length=20,primary_key=True,unique=True)
    first_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    USERNAME_FIELD = 'reg_no'
    REQUIRED_FIELDS=['first_name']
    objects = CustomUserManager()
    pic = models.ImageField(upload_to='profiles', default='/Dragonfruit.jpg')