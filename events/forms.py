from django import forms
from events.models import Events
from categories.models import Category
from users.models import User


class StyledFormMixin:
    """Mixing to apply style to form field"""

    default_classes = "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():  # type: ignore
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(
                    {
                        "class": self.default_classes,
                        "placeholder": f"Enter {field.label.lower()}",
                    }
                )
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes} resize-none",
                        "placeholder": f"Enter {field.label.lower()}",
                        "rows": 3,
                    }
                )
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside Date")
                field.widget.attrs.update(
                    {
                        "class": self.default_classes,
                    }
                )
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("Inside checkbox")
                field.widget.attrs.update({"class": "space-y-2"})
            else:
                print("Inside else")
                field.widget.attrs.update({"class": self.default_classes})


class EventsForm(StyledFormMixin, forms.ModelForm):
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
            "description": forms.Textarea(attrs={"rows": "2"}),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),
            "cover_url": forms.URLInput(),
        }

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()
