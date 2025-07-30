from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("", include("front.urls")),
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/categories/", include("categories.urls")),
    path("dashboard/events/", include("events.urls")),
    path("dashboard/users/", include("users.urls")),
    path("dashboard/group/", include("group.urls")),
] + debug_toolbar_urls()
