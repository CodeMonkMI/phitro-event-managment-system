from django.urls import path

from categories.views import index, create, single, update, delete

urlpatterns = [
    path("", index, name="category_index"),
    path("create/", create, name="category_create"),
    path("<uuid:id>/", single, name="category_view"),
    path("<uuid:id>/update/", update, name="category_update"),
    path("<uuid:id>/delete/", delete, name="category_delete"),
]
