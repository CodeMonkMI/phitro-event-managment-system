
import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from categories.models import Category

fake = Faker()

def seed_categories(n=10):
    for _ in range(n):
        Category.objects.create(
            name=fake.word(),
            description=fake.text()
        )
    print(f"{n} categories seeded successfully.")

if __name__ == "__main__":
    seed_categories()
