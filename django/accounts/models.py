from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    best_genre_id = models.IntegerField(null=True)