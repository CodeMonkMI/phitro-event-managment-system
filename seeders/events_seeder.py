
import os
import django
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evms.settings")
django.setup()

from events.models import Events
from categories.models import Category
from users.models import User
from seeders.images import image_urls

fake = Faker()

def seed_events(n=20):
    categories = list(Category.objects.all())
    users = list(User.objects.all())

    if not categories or not users:
        print("Please seed categories and users first.")
        return

    for _ in range(n):
        future_datetime = fake.date_time_between(
            start_date="+1d",  # ensures it's after today
            end_date="+90d"    # within next 3 months
        )
        event = Events.objects.create(
            name=fake.sentence(nb_words=4),
            description=fake.text(),
            date=future_datetime.date(),
            time=future_datetime.time(),
            location=fake.city(),
            category=random.choice(categories),
            cover_url=random.choice(image_urls)
        )
        event.participants.set(random.sample(users, k=random.randint(1, len(users))))
        print(f"a events seeded successfully.")

    print(f"{n} events seeded successfully.")

if __name__ == "__main__":
    seed_events()
