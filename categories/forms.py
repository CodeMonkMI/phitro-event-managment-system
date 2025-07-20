from django import forms
from categories.models import Category


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500",
                    "rows": "3",
                }
            ),
        }
