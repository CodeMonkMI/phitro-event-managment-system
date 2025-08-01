from django.urls import path

from front.views import (
    index,
    single,
    sign_up,
    sign_in,
    sign_out,
    not_found,
    no_permissions,
)

urlpatterns = [
    path("", index, name="front"),
    path("events/<uuid:id>", single, name="front_event_single"),
    path("sign-up", sign_up, name="sign_up"),
    path("sign-in", sign_in, name="sign_in"),
    path("sign-out", sign_out, name="sign_out"),
    path("not-found", not_found, name="not_found"),
    path("no_permissions", no_permissions, name="no_permissions"),
]
