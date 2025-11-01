
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from seeders.users_seeder import seed_users
from seeders.categories_seeder import seed_categories
from seeders.events_seeder import seed_events
from seeders.groups_seeder import seed_groups

from users.models import User
from categories.models import Category
from events.models import Events
from django.contrib.auth.models import Group

def truncate_data():
    print("Truncating existing data...")
    Events.objects.all().delete()
    Category.objects.all().delete()
    Group.objects.all().delete()
    User.objects.filter(is_staff=False, is_superuser=False).delete()
    print("Data truncated.")

if __name__ == "__main__":
    print("Seeding database...")
    truncate_data()
    seed_groups()
    seed_users()
    seed_categories()
    seed_events()
    print("Database seeded successfully.")
