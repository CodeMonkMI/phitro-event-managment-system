import re
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
            "profile_picture",
            "phone_number",
        ]
        widgets = {
            "username": forms.TextInput(),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number", "").strip()

        pattern = re.compile(r"^(\+8801[3-9]\d{8}|01[3-9]\d{8})$")
        if not pattern.match(phone):
            raise forms.ValidationError(
                "Enter a valid Bangladeshi mobile number: "
                "`+8801XXXXXXXXX` or `01XXXXXXXXX`."
            )
        return phone


class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)


class AssignRolesForm(StyledFormMixin, forms.ModelForm):

    class Meta:
        model = User
        fields = ["groups"]
        labels = {"groups": "Assign roles"}
