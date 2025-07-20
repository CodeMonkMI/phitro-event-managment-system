from django import forms
from users.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "name",
            "email",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                }
            ),
        }
