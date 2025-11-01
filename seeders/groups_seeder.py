
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from django.contrib.auth.models import Group

def seed_groups():
    groups = ["Admin", "Organizer", "Participant"]
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)
    print("Groups seeded successfully.")

if __name__ == "__main__":
    seed_groups()
