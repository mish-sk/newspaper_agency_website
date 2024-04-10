from django import forms
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor


class RedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )
