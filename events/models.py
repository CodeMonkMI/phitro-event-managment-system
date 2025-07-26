from django.db import models
from uuid import uuid4
from categories.models import Category
from users.models import User


# Create your models here.
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    cover_url = models.CharField(max_length=255)

    participants = models.ManyToManyField(User, related_name="events")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} is will be time: {self.time} , date: {self.date} at {self.location}"
