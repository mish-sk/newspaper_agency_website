from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorForm
from newspaper.models import Topic, Newspaper, Redactor


def index(request):
    topics = Topic.objects.all()
    newspapers = Newspaper.objects.all()
    redactors = Redactor.objects.all()
    context = {
        "topics": topics,
        "newspapers": newspapers,
        "redactors": redactors
    }
    return render(
        request,
        "newspaper/index.html",
        context=context
    )


class TopicListView(generic.ListView):
    model = Topic


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic_list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic_list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic_list")


class NewspaperListView(generic.ListView):
    model = Newspaper


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newspaper:newspaper_list")


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newspaper:newspaper_list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper_list")


class RedactorListView(generic.ListView):
    model = Redactor


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorForm


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspaper:redactor_list")


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor_list")
