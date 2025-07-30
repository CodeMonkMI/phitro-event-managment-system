from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.contrib.auth.models import Group
from group.forms import CreateGroupForm
from django.contrib import messages

# Create your views here.


def index(request):
    groups = Group.objects.all().order_by("name")
    print(groups)
    context = {"groups": groups}
    return render(request, "groups.html", context)


def create(request: HttpRequest):
    if request.method == "POST":

        form = CreateGroupForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            messages.success(request, "Role added successfully!")
            return redirect("groups")
        else:
            return render(request, "create_group.html", context)

    form = CreateGroupForm()
    context = {"form": form}
    return render(request, "create_group.html", context)


def update(request, name):

    try:
        group = Group.objects.filter(name=name).first()
        if group == None:
            raise Group.DoesNotExist("Role not found")
        if request.method == "POST":
            form = CreateGroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                messages.success(request, "Role details updated")
                return redirect("groups")

        form = CreateGroupForm(instance=group)
        context = {
            "form": form,
        }
        return render(request, "update_group.html", context)
    except Group.DoesNotExist:

        return redirect("not_found")


def delete(request, name):
    try:
        group = get_object_or_404(Group, name=name)
        if group == None:
            raise Group.DoesNotExist("Role not found")
        if request.method == "POST":
            messages.success(request, "Role deleted successfully!")
            group.delete()

        return redirect("groups")
    except Group.DoesNotExist:
        return redirect("not_found")
