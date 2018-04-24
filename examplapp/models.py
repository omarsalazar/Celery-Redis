from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
