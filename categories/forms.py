from django import forms
from categories.models import Category


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-200 outline-none px-3 py-2 rounded"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full border border-gray-200 px-3 py-2 rounded outline-none",
                    "rows": "2",
                }
            ),
        }
