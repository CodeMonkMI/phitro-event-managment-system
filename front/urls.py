from django.urls import path

from front.views import (
    SingleView,
    NotFoundView,
    NoPermissionView,
    ActivateUserView,
    FrontEventResponseView,
    IndexView,
    SignInView,
    SignUpView,
    SignOutView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="front"),
    path("events/<uuid:id>", SingleView.as_view(), name="front_event_single"),
    path(
        "events/<uuid:id>/response",
        FrontEventResponseView.as_view(),
        name="front_event_response",
    ),
    path("sign-up", SignUpView.as_view(), name="sign_up"),
    path("sign-in", SignInView.as_view(), name="sign_in"),
    path("sign-out", SignOutView.as_view(), name="sign_out"),
    path("not-found", NotFoundView.as_view(), name="not_found"),
    path("no_permissions", NoPermissionView.as_view(), name="no_permissions"),
    path(
        "activate/<uuid:user_id>/<str:token>",
        ActivateUserView.as_view(),
        name="activate_user",
    ),
]
