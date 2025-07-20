from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from users.models import User
from users.forms import UserForm

# Create your views here.


def index(request):
    users = User.objects.filter().order_by("created_at")
    context = {"users": users}
    return render(request, "users.html", context)


def create(request: HttpRequest):
    if request.method == "POST":

        form = UserForm(request.POST)
        context = {}
        if form.is_valid():
            form.save()
            context["message"] = "users created successfully"

        return redirect("users_index")

    form = UserForm()
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
            form = UserForm(request.POST, instance=event)
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

        form = UserForm(instance=event)
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
