import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from users.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

fake = Faker()


def seed_users(n=10):
    # Seed hardcoded users
    users_data = [
        {
            "username": "admin",
            "password": "pass1234",
            "email": "admin@example.com",
            "is_staff": True,
            "is_superuser": True,
            "group": "Admin",
        },
        {
            "username": "manager",
            "password": "pass1234",
            "email": "manager@example.com",
            "is_staff": True,
            "is_superuser": False,
            "group": "Organizer",
        },
        {
            "username": "user1",
            "password": "pass1234",
            "email": "user1@example.com",
            "is_staff": False,
            "is_superuser": False,
            "group": "Participant",
        },
        {
            "username": "user2",
            "password": "pass1234",
            "email": "user2@example.com",
            "is_staff": False,
            "is_superuser": False,
            "group": "Participant",
        },
    ]

    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults={
                "password": make_password(user_data["password"]),
                "email": user_data["email"],
                "is_staff": user_data["is_staff"],
                "is_superuser": user_data["is_superuser"],
            },
        )
        if user:
            group = Group.objects.get(name=user_data["group"])
            user.groups.add(group)

    # Seed random users
    participant_group = Group.objects.get(name="Participant")
    for _ in range(n):
        user = User.objects.create(
            username=fake.user_name(),
            password=make_password("password"),
            email=fake.email(),
        )
        user.groups.add(participant_group)

    print(f"{n} random users seeded successfully.")


if __name__ == "__main__":
    seed_users()
