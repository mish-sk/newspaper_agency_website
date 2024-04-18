from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple

from newspaper.models import Redactor, Newspaper, Topic


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


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search topic"})
    )


class RedactorSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search first_name"})
    )


class NewspaperSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Title or Content"})
    )
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        required=False,
        label="Filter by Topic",
        empty_label="All Topics"
    )