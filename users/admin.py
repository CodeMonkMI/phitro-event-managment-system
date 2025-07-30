from django.contrib import admin
from categories.models import Category
from events.models import Events
from users.models import User


# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Events)
