from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("dashboard/", include("dashboard.urls")),
    path("admin/", admin.site.urls),
    path("categories/", include("categories.urls")),
    path("events/", include("events.urls")),
    path("users/", include("users.urls")),
] + debug_toolbar_urls()
