from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profile_picture = models.ImageField(
        upload_to="users_image",
        blank=True,
        null=True,
        default="users_image/default_user.jpg",
    )
    phone_number = models.CharField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
