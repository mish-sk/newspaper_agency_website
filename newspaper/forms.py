from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple

from newspaper.models import Redactor, Newspaper


class RedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'published_date', 'topic', 'publishers']
        widgets = {
            'publishers': CheckboxSelectMultiple,
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
