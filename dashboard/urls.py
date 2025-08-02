from django.urls import path

from dashboard.views import index, dashboard_route

urlpatterns = [
    path("", index, name="dashboard"),
    path("dashboard-routing", dashboard_route, name="dashboard_routing"),
]
