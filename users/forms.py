from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.mixin import StyledFormMixin
from django.contrib.auth.models import Group


class RegistrationForm(StyledFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(),
        }


class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)


class AssignRolesForm(StyledFormMixin, forms.ModelForm):

    class Meta:
        model = User
        fields = ["groups"]
        labels = {"groups": "Assign roles"}
