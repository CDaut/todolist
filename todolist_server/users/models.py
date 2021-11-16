import django.contrib.auth.models
from django.db import models


# Create your models here.
class ApplicationUser(models.Model):
    auth_user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
