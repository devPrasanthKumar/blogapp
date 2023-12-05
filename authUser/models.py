from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)
    number = models.IntegerField(default=None, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    USER_CHOICES = [("Normal User", "User Mode"),
                    ("Content Creator", "Creator Mode")]

    user_choice = models.CharField(max_length=40, choices=USER_CHOICES)
