import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.topic = Topic.objects.create(
            name="test_topic"
        )
        self.redactor = get_user_model().objects.create(
            username="redactor_user",
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

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "test_topic")

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} ({self.redactor.first_name} {self.redactor.last_name}), "
            f"years of experience: {self.redactor.years_of_experience}."
        )

    def test_newspaper_str(self):
        self.assertEqual(
            str(self.newspaper),
            f"test_title ({datetime.datetime.today().date()})"
        )
