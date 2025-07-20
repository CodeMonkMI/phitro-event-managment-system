from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from events.models import Events
from events.forms import EventsForm

# Create your views here.


def index(request):
    events = Events.objects.filter().order_by("created_at")
    context = {"events": events}
    return render(request, "events.html", context)


def create(request: HttpRequest):
    if request.method == "POST":

        form = EventsForm(request.POST)
        context = {}
        if form.is_valid():
            form.save()
            context["message"] = "events created successfully"

        return render(request, "create_events.html", context)

    form = EventsForm()
    context = {"form": form}
    return render(request, "create_events.html", context)


def single(request: HttpRequest, id):
    try:
        event = Events.objects.get(pk=id)

        context = {"event": event}
        return render(request, "single.html", context)
    except Events.DoesNotExist:
        return render(request, "single.html")


def update(request, id):

    try:
        event = Events.objects.get(pk=id)
        if request.method == "POST":
            form = EventsForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                context = {
                    "isFound": True,
                    "form": form,
                    "event": event,
                    "id": id,
                    "message": "events updated successfully",
                }
                return render(request, "update.html", context)

        form = EventsForm(instance=event)
        context = {
            "isFound": True,
            "form": form,
            "id": id,
            "event": event,
        }
        return render(request, "update.html", context)
    except Events.DoesNotExist:
        return render(request, "update.html")


def delete(request, id):
    try:
        event = get_object_or_404(Events, id=id)

        if request.method == "POST":
            event.delete()

        return redirect("index")
    except Events.DoesNotExist:
        return redirect("index")
