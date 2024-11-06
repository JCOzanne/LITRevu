from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser (AbstractUser):
    follows=models.ManyToManyField(
        'self',
        symmetrical=True,
        verbose_name='suit'
    )

