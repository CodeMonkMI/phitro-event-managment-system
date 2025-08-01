from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.db.models import Count
from events.models import Events
from users.models import User
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from users.middleware import is_admin

# Create your views here.


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def index(request):
    base_events = Events.objects.select_related("category").prefetch_related(
        "participants"
    )
    total_events = base_events.count()

    upcoming_events = base_events.filter(date__gte=date.today())
    past_events = base_events.filter(date__lte=date.today())
    total_upcoming_events = upcoming_events.count()
    total_past_events = past_events.count()
    total_participants = User.objects.filter(events__isnull=False).distinct().count()

    events = base_events.filter(date=date.today())
    title_value = "Today's"

    events_type = request.GET.get("events_type")
    if events_type == "all":
        events = base_events.all()
        title_value = "Total"
    elif events_type == "up":
        events = upcoming_events
        title_value = "Upcoming"
    elif events_type == "past":
        events = past_events
        title_value = "Past"

    context = {
        "total_events": total_events,
        "total_upcoming_events": total_upcoming_events,
        "total_past_events": total_past_events,
        "total_participants": total_participants,
        "events": events,
        "title_value": title_value,
    }
    return render(request, "dashboard.html", context)
