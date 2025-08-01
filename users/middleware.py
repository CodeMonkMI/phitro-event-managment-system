from users.models import User
from django.db.models import Q


def is_admin(user):
    return user.groups.filter(name="Admin").exists()


def is_organizer(user):
    return user.groups.filter(Q(name="Organizer") | Q(name="Admin")).exists()


def is_participant(user: User):
    return user.groups.filter(name="Participant").exists()
