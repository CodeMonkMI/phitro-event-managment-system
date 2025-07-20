from django import forms
from events.models import Events
from categories.models import Category
from users.models import User


class EventsForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # adjust as needed
        widget=forms.Select(attrs={"class": "w-full border ..."}),
    )
    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),  # adjust as needed
        widget=forms.SelectMultiple(attrs={"class": "w-full border ..."}),
    )

    class Meta:
        model = Events
        fields = [
            "name",
            "description",
            "date",
            "time",
            "location",
            "cover_url",
            "category",
            "participants",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border ..."}),
            "description": forms.Textarea(
                attrs={"class": "w-full border ...", "rows": "2"}
            ),
            "date": forms.DateInput(
                attrs={"type": "date", "class": "w-full border ..."}
            ),
            "time": forms.TimeInput(
                attrs={"type": "time", "class": "w-full border ..."}
            ),
            "location": forms.TextInput(attrs={"class": "w-full border ..."}),
            "cover_url": forms.URLInput(attrs={"class": "w-full border ..."}),
            # "category" and "participants" handled above, no need here
        }
