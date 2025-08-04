from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from users.models import User
from users.forms import RegistrationForm, AssignRolesForm
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from users.middleware import is_admin

# Create your views here.


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def index(request):
    users = (
        User.objects.annotate(nums_event=Count("events"))
        .filter()
        .order_by("date_joined")
    )
    context = {"users": users}
    return render(request, "users.html", context)


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def create(request: HttpRequest):
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect("users_index")
        else:
            return render(request, "create_user.html", context)

    form = RegistrationForm()
    context = {"form": form}
    return render(request, "create_user.html", context)


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def single(request: HttpRequest, id):
    try:
        user = User.objects.get(pk=id)

        context = {"user": user}
        # todo include events later
        return render(request, "single_user.html", context)
    except User.DoesNotExist:
        return render(request, "single_user.html")


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def update(request, id):

    try:
        user = User.objects.get(pk=id)
        if request.method == "POST":
            form = AssignRolesForm(request.POST)
            if form.is_valid():
                roles = form.cleaned_data["groups"]
                user.groups.set(roles)
                messages.success(request, "Users updated successfully!")
                return redirect("users_index")

        form = AssignRolesForm(instance=user)
        context = {
            "form": form,
        }
        return render(request, "assign_user_role.html", context)
    except User.DoesNotExist:
        return redirect("not_found")


@login_required
@user_passes_test(is_admin, login_url="no_permissions")
def delete(request, id):
    try:
        event = get_object_or_404(User, id=id)

        if request.method == "POST":
            event.delete()

        return redirect("users_index")
    except User.DoesNotExist:
        return redirect("users_index")


@login_required
def auth_user_profile(request: HttpRequest):
    try:
        user = User.objects.get(pk=request.user.pk)
        print(user.id)
        context = {
            "name": f"{user.first_name} {user.last_name}",
            "profile_picture": user.profile_picture.url,
            "email": user.email,
            "username": user.username,
            "last_login": user.last_login,
            "joined": user.date_joined,
            "phone_number": user.phone_number,
        }

        return render(request, "user_profile.html", context)
    except User.DoesNotExist:
        return render(request, "user_profile.html")
