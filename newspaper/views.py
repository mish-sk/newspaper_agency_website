from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.models import Topic, Newspaper, Redactor
from newspaper_agency_website import settings


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
