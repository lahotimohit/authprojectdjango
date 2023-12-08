from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='images/profile_photo', blank=True, null=True, default="avatar.svg")
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []