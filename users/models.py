from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToUniquePath:
    """
    Callable that builds a path like:
      users_image/<uuid4>.<ext>
    or if you prefer,
      users_image/<username>_<uuid4>.<ext>
    """

    def __init__(self, base_path="users_image"):
        self.base_path = base_path

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1].lower()
        unique_name = uuid.uuid4().hex
        new_filename = f"{unique_name}{ext}"
        return os.path.join(self.base_path, new_filename)


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profile_picture = models.ImageField(
        upload_to=UploadToUniquePath("users_image"),
        blank=True,
        null=True,
        default="users_image/default_user.jpg",
    )
    phone_number = models.CharField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
