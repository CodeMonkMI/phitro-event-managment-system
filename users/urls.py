from django.urls import path

from users.views import (
    index,
    create,
    single,
    update,
    delete,
    auth_user_profile,
    AuthUserProfileUpdateView,
    AuthUserPasswordChangeView,
)

from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path("", index, name="users_index"),
    path("create/", create, name="users_create"),
    path("<uuid:id>/", single, name="users_view"),
    path("<uuid:id>/update/", update, name="users_update"),
    path("<uuid:id>/delete/", delete, name="users_delete"),
    path("me", auth_user_profile, name="auth_user_profile"),
    path(
        "me/update",
        AuthUserProfileUpdateView.as_view(),
        name="auth_user_profile_update",
    ),
    path(
        "me/password-change",
        AuthUserPasswordChangeView.as_view(),
        name="auth_user_password_change",
    ),
    path(
        "me/password-change/done",
        PasswordChangeDoneView.as_view(),
        name="auth_user_password_change_done",
    ),
]
