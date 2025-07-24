from django.urls import path

from front.views import index, single

urlpatterns = [
    path("", index, name="front"),
    path("events/<uuid:id>", single, name="front_event_single"),
]
