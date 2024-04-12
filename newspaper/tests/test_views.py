import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from newspaper.models import Topic, Newspaper


class PublicNewspaperViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("newspaper:index"))
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_list_login_required(self):
        response = self.client.get(reverse("newspaper:newspaper_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_detail_login_required(self):
        response = self.client.get(reverse("newspaper:newspaper_detail", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_create_login_required(self):
        response = self.client.get(reverse("newspaper:newspaper_create"))
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_delete_login_required(self):
        response = self.client.get(reverse("newspaper:newspaper_delete", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_update_login_required(self):
        response = self.client.get(reverse("newspaper:newspaper_update", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_list_login_required(self):
        response = self.client.get(reverse("newspaper:redactor_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_detail_login_required(self):
        response = self.client.get(reverse("newspaper:redactor_detail", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_create_login_required(self):
        response = self.client.get(reverse("newspaper:redactor_create"))
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_delete_login_required(self):
        response = self.client.get(reverse("newspaper:redactor_delete", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_update_login_required(self):
        response = self.client.get(reverse("newspaper:redactor_update", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_topic_list_login_required(self):
        response = self.client.get(reverse("newspaper:topic_list"))
        self.assertNotEqual(response.status_code, 200)

    def test_topic_create_login_required(self):
        response = self.client.get(reverse("newspaper:topic_create"))
        self.assertNotEqual(response.status_code, 200)

    def test_topic_delete_login_required(self):
        response = self.client.get(reverse("newspaper:topic_delete", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)

    def test_topic_update_login_required(self):
        response = self.client.get(reverse("newspaper:topic_update", kwargs={"pk": 1}))
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperViewTest(TestCase):
    def setUp(self) -> None:
        self.topic = Topic.objects.create(
            name="test_topic_name"
        )
        self.redactor = get_user_model().objects.create(
            username="redactor",
            password="test_password1234",
            first_name="Test",
            last_name="Redactor",
            years_of_experience=5,
        )
        self.newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            published_date=datetime.datetime.today().date(),
            topic=self.topic,
        )
        self.newspaper.publishers.add(self.redactor)
        self.client.force_login(self.redactor)

    def test_redactor_detail(self):
        response = self.client.get(
            reverse("newspaper:redactor_detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_retrieve_redactors(self):
        response = self.client.get(reverse("newspaper:redactor_list"))
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(get_user_model().objects.all())
        )
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")

    def test_newspaper_detail(self):
        response = self.client.get(
            reverse("newspaper:newspaper_detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_retrieve_newspapers(self):
        response = self.client.get(reverse("newspaper:newspaper_list"))
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.all())
        )
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")

    def test_retrieve_topics(self):
        response = self.client.get(reverse("newspaper:topic_list"))
        self.assertEqual(
            list(response.context["topic_list"]),
            list(Topic.objects.all())
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")

