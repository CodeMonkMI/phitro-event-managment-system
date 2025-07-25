from django.shortcuts import render
from events.models import Events
from django.db.models import Count, Q
from datetime import date
import random

events_images = [
    "https://plus.unsplash.com/premium_photo-1661306437817-8ab34be91e0c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1556125574-d7f27ec36a06?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1464047736614-af63643285bf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1478147427282-58a87a120781?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://plus.unsplash.com/premium_photo-1681487469745-91d1d8a5836b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZXZlbnRzfGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1549451371-64aa98a6f660?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1672354234377-38ef695dd2ed?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1643759543584-fb6f448d42d4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1531058020387-3be344556be6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1664302654457-399bf1bff533?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1661486750841-c02a9d22a1a6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1515169067868-5387ec356754?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjl8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1686783007953-4fcb40669dd8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzZ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1664303677453-ca2ad8f7dd8d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDJ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDV8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1599943821034-8cb5c7526922?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTZ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NjR8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1665672231047-34208112af96?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NzN8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1625062798671-a2b45295b6e7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NzZ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1528605105345-5344ea20e269?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nzl8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1636293235717-7895bf07abc8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODN8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1561489401-fc2876ced162?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTF8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
    "https://images.unsplash.com/photo-1571645163064-77faa9676a46?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTZ8fGV2ZW50c3xlbnwwfHwwfHx8MA%3D%3D",
]


# Create your views here.
def index(request):
    name = request.GET.get("name")
    location = request.GET.get("location")

    events = (
        Events.objects.select_related("category")
        .prefetch_related("participants")
        .annotate(nums_participants=Count("participants"))
        .order_by("-date")
    )

    if name != None and name != "":
        events = events.filter(name__icontains=name)
    if location != None and location != "":
        events = events.filter(location__icontains=location)

    context = {
        "events": events,
    }
    return render(request, "front.html", context)


def single(request, id):
    try:
        event = (
            Events.objects.prefetch_related("participants")
            .select_related("category")
            .get(pk=id)
        )
        related_events = (
            Events.objects.select_related("category")
            .prefetch_related("participants")
            .annotate(nums_participants=Count("participants"))
            .order_by("-date")[:4]
        )

        images = random.sample(events_images, 6)

        context = {
            "event": event,
            "related_events": related_events,
            "images": images,
        }
        return render(request, "front_event_single.html", context)
    except Events.DoesNotExist:
        return render(request, "front_event_single.html")
