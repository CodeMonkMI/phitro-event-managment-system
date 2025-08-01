from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from categories.models import Category
from categories.forms import CategoriesForm
from django.contrib.auth.decorators import login_required, user_passes_test
from users.middleware import is_organizer

# Create your views here.


@login_required
@user_passes_test(is_organizer, login_url="no_permissions")
def index(request):
    categories = (
        Category.objects.prefetch_related("events").filter().order_by("created_at")
    )
    context = {"categories": categories}
    return render(request, "index.html", context)


@login_required
@user_passes_test(is_organizer, login_url="no_permissions")
def create(request: HttpRequest):
    if request.method == "POST":

        form = CategoriesForm(request.POST)
        context = {}
        if form.is_valid():
            form.save()
            context["message"] = "Category created successfully"
            return redirect("category_index")
        else:
            context = {"form": form}
            return render(request, "create.html", context)

    form = CategoriesForm()
    context = {"form": form}
    return render(request, "create.html", context)


@login_required
@user_passes_test(is_organizer, login_url="no_permissions")
def single(request: HttpRequest, id):
    try:
        category = Category.objects.get(pk=id)

        context = {"category": category}
        return render(request, "single_category.html", context)
    except Category.DoesNotExist:
        return render(request, "single_category.html")


@login_required
@user_passes_test(is_organizer, login_url="no_permissions")
def update(request, id):

    try:
        category = Category.objects.get(pk=id)
        if request.method == "POST":
            form = CategoriesForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                context = {
                    "isFound": True,
                    "form": form,
                    "category": category,
                    "id": id,
                    "message": "Category updated successfully",
                }
                return redirect("category_index")

        form = CategoriesForm(instance=category)
        context = {
            "isFound": True,
            "form": form,
            "id": id,
            "category": category,
        }
        return render(request, "update.html", context)
    except Category.DoesNotExist:
        return render(request, "update.html")


@login_required
@user_passes_test(is_organizer, login_url="no_permissions")
def delete(request, id):
    try:
        category = get_object_or_404(Category, id=id)

        if request.method == "POST":
            category.delete()

        return redirect("category_index")
    except Category.DoesNotExist:
        return redirect("category_index")
