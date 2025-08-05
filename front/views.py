from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from events.models import Events
from django.db.models import Count
import random
from users.forms import RegistrationForm, LoginForm
from django.contrib import messages
from users.models import User
from django.contrib.auth.tokens import default_token_generator
from django.views.generic import ListView, FormView, TemplateView, DetailView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .data import events_images
from django.http import Http404
from front.forms import CustomPasswordResetForm, CustomSetPasswordForm


# Event related views
class IndexView(ListView):
    model = Events
    template_name = "front.html"
    context_object_name = "events"

    def get_queryset(self):

        name = self.request.GET.get("name")
        location = self.request.GET.get("location")

        qs = (
            Events.objects.select_related("category")
            .prefetch_related("participants")
            .annotate(nums_participants=Count("participants"))
            .order_by("-date")
        )

        if name != None and name != "":
            qs = qs.filter(name__icontains=name)
        if location != None and location != "":
            qs = qs.filter(location__icontains=location)

        return qs


class SingleView(DetailView):
    pk_url_kwarg = "id"
    template_name = "front_event_single.html"
    model = Events
    context_object_name = "event"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect("not_found")

    def get_queryset(self):
        return Events.objects.prefetch_related("participants").select_related(
            "category"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        context["related_events"] = (
            Events.objects.select_related("category")
            .prefetch_related("participants")
            .annotate(nums_participants=Count("participants"))
            .order_by("-date")[:4]
        )
        context["images"] = random.sample(events_images, 6)

        user = self.request.user
        context["is_participating"] = (
            user.is_authenticated and event.participants.filter(pk=user.pk).exists()  # type: ignore
        )
        return context


class FrontEventResponseView(LoginRequiredMixin, DetailView):
    template_name = ""
    pk_url_kwarg = "id"
    context_object_name = "event"
    model = Events

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        user = request.user
        if not event.participants.filter(pk=user.pk).exists():  # type: ignore
            event.participants.add(user)  # type: ignore
            msg = "Thanks you for joining this event!"
            messages.success(request, msg)
        return redirect("front_event_single", id=event.id)  # type: ignore


# auth related views
class SignInView(LoginView):
    template_name = "sign_in.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "You provided credentials are invalid!")
        return super().form_invalid(form)


class SignUpView(FormView):
    template_name = "sign_up.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("sign_in")

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("dashboard_routing")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        messages.success(
            self.request, "Sign up successfully! Activate you account before sign in!"
        )
        return super().form_valid(form)


class ActivateUserView(View):

    def get(self, request, user_id, token, *args, **kwargs):
        try:
            user = User.objects.get(pk=user_id)
            if not default_token_generator.check_token(user, token):
                raise Exception("Invalid!")

            user.is_active = True
            user.save()
            messages.success(request, "You account is activated. Now you can sign in")
            return redirect("sign_in")

        except Exception as e:
            return redirect("not_found")


class SignOutView(LogoutView):
    template_name = "sign_in.html"


# other views
class NotFoundView(TemplateView):
    template_name = "not_found.html"


class NoPermissionView(LoginRequiredMixin, TemplateView):
    template_name = "no_permissions.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "custom_password_reset.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("password_reset")
    email_template_name = "email/password_reset_email.html"

    def form_valid(self, form):
        messages.success(self.request, "We have send you email. Please check you inbox")
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "custom_password_reset_confirm.html"
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy("sign_in")

    def form_valid(self, form):
        messages.success(
            self.request, "You password reset successfully. Sign to proceed further."
        )
        return super().form_valid(form)
