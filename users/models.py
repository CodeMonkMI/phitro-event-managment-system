from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self) -> str:
        return self.username
