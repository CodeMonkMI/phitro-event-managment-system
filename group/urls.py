from django.urls import path

from group.views import index, create, update, delete

urlpatterns = [
    path("", index, name="groups"),
    path("create/", create, name="group_create"),
    path("<str:name>/update/", update, name="group_update"),
    path("<str:name>/delete/", delete, name="group_delete"),
]
