from django.urls import path

from events.views import index, create, single, update, delete

urlpatterns = [
    path("", index, name="events_index"),
    path("create/", create, name="events_create"),
    path("<uuid:id>/", single, name="events_view"),
    path("<uuid:id>/update/", update, name="events_update"),
    path("<uuid:id>/delete/", delete, name="events_delete"),
]
