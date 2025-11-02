from django.urls import path

from front.views import (
    SingleView,
    NotFoundView,
    NoPermissionView,
    ActivateUserView,
    FrontEventResponseView,
    EventsView,
    SignInView,
    SignUpView,
    SignOutView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    HomeView,
    ContactUsView,
    AboutUsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="front"),
    path("contact-us", ContactUsView.as_view(), name="front_contact"),
    path("about-us", AboutUsView.as_view(), name="front_about"),
    path("events", EventsView.as_view(), name="front_events"),
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
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
