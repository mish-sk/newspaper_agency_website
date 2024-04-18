from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorForm, NewspaperForm, TopicSearchForm, NewspaperSearchForm, RedactorSearchForm
from newspaper.models import Topic, Newspaper, Redactor


@login_required
def index(request):
    topics = Topic.objects.all()
    newspapers = Newspaper.objects.all()
    redactors = Redactor.objects.all()

    top_active_redactors = redactors.annotate(num_newspapers=Count('newspaper__publishers')).order_by('-num_newspapers')[:5]
    recent_newspapers = newspapers.order_by('-published_date')[:5]
    most_popular_topics = topics.annotate(num_newspapers=Count("newspaper")).order_by("-num_newspapers")[:5]

    context = {
        "topics": topics,
        "newspapers": newspapers,
        "redactors": redactors,
        "top_active_redactors": top_active_redactors,
        "recent_newspapers": recent_newspapers,
        "most_popular_topics": most_popular_topics,
    }
    return render(
        request,
        "newspaper/index.html",
        context=context
    )


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic_list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic_list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic_list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 10

    def get_queryset(self) -> QuerySet:
        queryset = Newspaper.objects.all()

        topic_id = self.request.GET.get('topic')
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)

        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('name')

            topic = form.cleaned_data.get('topic')

            if query:
                queryset = queryset.filter(title__icontains=query) | queryset.filter(content__icontains=query)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("name", "")
        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        context["topics"] = Topic.objects.all()
        return context

class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper_list")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        updated_newspaper_id = self.object.pk
        return reverse_lazy("newspaper:newspaper_detail", kwargs={"pk": updated_newspaper_id})


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper_list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspaper:redactor_list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        updated_redactor_id = self.object.pk
        return reverse_lazy("newspaper:redactor_detail", kwargs={"pk": updated_redactor_id})


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor_list")
