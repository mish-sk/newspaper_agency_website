from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorCreateView,
    RedactorDetailView,
    RedactorUpdateView,
    RedactorDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper_list"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper_create"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper_detail"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper_update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper_delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor_list"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor_create"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor_detail"),
    path("redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor_update"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor_delete"),
]

app_name = "newspaper"
