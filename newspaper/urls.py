from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
]

app_name = "newspaper"
