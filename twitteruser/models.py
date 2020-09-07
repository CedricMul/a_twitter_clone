from django.db import models
from django.contrib.auth.models import AbstractUser

class MyTwitterUser(AbstractUser):
    following = models.ManyToManyField(
        'self',
        related_name='following_users',
        blank=True,
        symmetrical=False
    )
