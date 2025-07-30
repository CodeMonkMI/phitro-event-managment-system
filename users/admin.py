from django.contrib import admin
from categories.models import Category
from events.models import Events


# Register your models here.
admin.site.register(Category)
admin.site.register(Events)
