from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13,default='')
    CHOICES = (
        (1,'admin'),
        (2,'user'),
        (3,'adib'),
    )
    roles = models.PositiveIntegerField(default=1,choices=CHOICES)
