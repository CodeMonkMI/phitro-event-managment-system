from django.urls import path

from categories.views import index, create, single, update, delete

urlpatterns = [
    path("", index, name="categories:index"),
    path("create/", create, name="categories:create"),
    path("<uuid:id>/", single, name="categories:view"),
    path("<uuid:id>/update/", update, name="categories:update"),
    path("<uuid:id>/delete/", delete, name="categories:delete"),
]
