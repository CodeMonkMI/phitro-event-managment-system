from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from users.models import User
from users.forms import RegistrationForm
from django.db.models import Count

# Create your views here.


def index(request):
    users = (
        User.objects.annotate(nums_event=Count("events"))
        .filter()
        .order_by("date_joined")
    )
    context = {"users": users}
    return render(request, "users.html", context)


def create(request: HttpRequest):
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("users_index")
        else:
            return render(request, "create_user.html", context)

    form = RegistrationForm()
    context = {"form": form}
    return render(request, "create_user.html", context)


def single(request: HttpRequest, id):
    try:
        user = User.objects.get(pk=id)

        context = {"user": user}
        # todo include events later
        return render(request, "single_user.html", context)
    except User.DoesNotExist:
        return render(request, "single_user.html")


def update(request, id):

    try:
        event = User.objects.get(pk=id)
        if request.method == "POST":
            form = RegistrationForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                context = {
                    "isFound": True,
                    "form": form,
                    "event": event,
                    "id": id,
                    "message": "users updated successfully",
                }
                return redirect("users_index")

        form = RegistrationForm(instance=event)
        context = {
            "isFound": True,
            "form": form,
            "id": id,
            "event": event,
        }
        return render(request, "update_user.html", context)
    except User.DoesNotExist:
        return render(request, "update_user.html")


def delete(request, id):
    try:
        event = get_object_or_404(User, id=id)

        if request.method == "POST":
            event.delete()

        return redirect("users_index")
    except User.DoesNotExist:
        return redirect("users_index")
