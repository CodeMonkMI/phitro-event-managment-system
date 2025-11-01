
import os
import django
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from events.models import Events
from categories.models import Category
from users.models import User

fake = Faker()

def seed_events(n=20):
    categories = list(Category.objects.all())
    users = list(User.objects.all())

    if not categories or not users:
        print("Please seed categories and users first.")
        return

    for _ in range(n):
        event = Events.objects.create(
            name=fake.sentence(nb_words=4),
            description=fake.text(),
            date=fake.date_this_year(after_today=True),
            time=fake.time(),
            location=fake.city(),
            category=random.choice(categories)
        )
        event.participants.set(random.sample(users, k=random.randint(1, len(users))))
        print(f"a events seeded successfully.")

    print(f"{n} events seeded successfully.")

if __name__ == "__main__":
    seed_events()
