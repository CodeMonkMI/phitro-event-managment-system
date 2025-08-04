from django.urls import path

from users.views import index, create, single, update, delete, auth_user_profile

urlpatterns = [
    path("", index, name="users_index"),
    path("create/", create, name="users_create"),
    path("<uuid:id>/", single, name="users_view"),
    path("<uuid:id>/update/", update, name="users_update"),
    path("<uuid:id>/delete/", delete, name="users_delete"),
    path("me", auth_user_profile, name="auth_user_profile"),
]
