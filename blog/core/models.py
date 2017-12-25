from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    email = models.EmailField(default='', max_length=255)
